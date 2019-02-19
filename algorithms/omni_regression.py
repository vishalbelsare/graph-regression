# omni_regression.py
# Vivek Gopalakrishnan
# 2019-02-16

import warnings

import graspy as gs
from importlib import import_module

class OmniRegression():
    """
    Regressing covariates out of a graph embedding.

    Parameters
    ----------
    model : {'LinearRegression' (default), 'RandomForestRegressor'}, optional
        Desired model for regression.

    Attributes
    ----------

    """

    def __init__(self, model="LinearRegression"):

        supported_models = ['LinearRegression', 'RandomForestRegressor']
        if model in supported_models:
            self.model = self._import_model_module(model)
        else:
            msg = "Please select an algorithm from {}.".format(supported_models)
            raise ValueError(msg)


    def _import_model_module(self):
        """
        Import and initialize model from sklearn given string.
        """
        from sklearn.linear_model import LinearRegression
        if self.model == 'LinearRegression':
            module = import_module('sklearn.linear_model')
            LinearRegression = getattr(module, self.model)
            return LinearRegression()
        if self.model == 'RandomForestRegressor':
            module = import_module('sklearn.ensemble')
            RandomForestRegressor = getattr(module, self.model)
            return RandomForestRegressor(n_estimators=500)


    def fit(self, embedding, covariates):
        """
        Fit the model with an embedding and covariates
        """

        # Check embedding and array of covariates have appropriate shapes
        assert embedding.shape[0] == covariates.shape[0]

        # Fit model and subtract out covariates
        self.model.fit(covariates, embedding)
        return embdding - model.predict(covariates)
