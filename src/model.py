
import pymc as pm
import pytensor.tensor as pt
import numpy as np

class ChangePointModel:
    def __init__(self, returns):
        self.returns = returns.astype("float32")  # Safe float32
        self.model = None
        self.idata = None

    def build_model(self):
        n = len(self.returns)
        idx = np.arange(n).astype("int32")  # Critical: must be int32

        with pm.Model() as self.model:
            # Safe cast: convert Python int to PyTensor constant
            lower = pt.as_tensor_variable(np.int32(0))
            upper = pt.as_tensor_variable(np.int32(n - 1))
            tau = pm.DiscreteUniform("tau", lower=lower, upper=upper)

            mu1 = pm.Normal("mu1", mu=pt.constant(0.0, dtype="float32"), sigma=pt.constant(1.0, dtype="float32"))
            mu2 = pm.Normal("mu2", mu=pt.constant(0.0, dtype="float32"), sigma=pt.constant(1.0, dtype="float32"))

            sigma = pm.HalfNormal("sigma", sigma=pt.constant(1.0, dtype="float32"))

            mu = pt.switch(tau >= idx, mu1, mu2)

            pm.Normal("obs", mu=mu, sigma=sigma, observed=self.returns)

    def run_inference(self, draws=2000, tune=1000):
        if self.model is None:
            raise ValueError("Model not built yet. Call build_model() first.")
        with self.model:
            self.idata = pm.sample(draws=draws, tune=tune, return_inferencedata=True)

    def get_posterior(self):
        return self.idata
