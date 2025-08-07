import pymc as pm
import numpy as np
import pytensor.tensor as pt

class ChangePointModel:
    def __init__(self, returns):
        self.returns = returns.astype(np.float32)  # Cast early to avoid dtype issues
        self.model = None
        self.idata = None

    def build_model(self):
        n = len(self.returns)
        idx = np.arange(n).astype("int32")  # Cast index to int32 explicitly

        with pm.Model() as self.model:
            tau = pm.DiscreteUniform("tau", lower=0, upper=n - 1)

            mu1 = pm.Normal("mu1", mu=0.0, sigma=1.0)
            mu2 = pm.Normal("mu2", mu=0.0, sigma=1.0)

            sigma = pm.HalfNormal("sigma", sigma=1.0)

            mu = pt.switch(tau >= idx, mu1, mu2)

            pm.Normal("obs", mu=mu, sigma=sigma, observed=self.returns)

    def run_inference(self, draws=2000, tune=1000):
        if self.model is None:
            raise ValueError("Model not built yet. Call build_model() first.")
        with self.model:
            self.idata = pm.sample(draws=draws, tune=tune, return_inferencedata=True)

    def get_posterior(self):
        return self.idata
