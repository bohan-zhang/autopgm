from pgmpy.models import BayesianModel


class BayesianMerger(object):
    def __init__(self, models):
        self.models = models
        self.edges = set()
        self.cpds = {}
        self.model = None

    def merge(self):
        for model in self.models:
            # edges
            self.edges.update(model.edges)
            # cpds
            for cpd in model.get_cpds():
                if cpd.variable not in self.cpds.keys():
                    self.cpds[cpd.variable] = cpd
                else:
                    # TODO: this is temporary; we should consider how to approach this problem
                    self.cpds[cpd.variable] = cpd

        # new model
        self.model = BayesianModel(self.edges)
        self.model.add_cpds(list(self.cpds.values()))

        if self.model.check_model():
            return self.model
        else:
            # TODO: raise errors
            return None