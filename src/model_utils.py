import matplotlib.pyplot as plt
import arviz as az

def plot_trace(idata):
    """
    Plots the trace of all variables.
    """
    az.plot_trace(idata, figsize=(10, 6))
    plt.tight_layout()
    plt.show()

def plot_posterior_tau(idata):
    """
    Plots the posterior histogram of the change point tau.
    """
    tau_posterior = idata.posterior['tau'].values.flatten()

    plt.figure(figsize=(10, 4))
    plt.hist(tau_posterior, bins=30, color='skyblue', edgecolor='black')
    plt.title("Posterior Distribution of Change Point (τ)")
    plt.xlabel("Day Index")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
