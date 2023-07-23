class investmentOption:
    """
    This class should gather all information about a investment option, defined by each column in the csv file.
    """

    def __init__(self, id: int, description: str, cost: int, payback: int, risk: int):
        """
        :param id: option identifier.
        :param description: investment specification.
        :param cost: investment cost.
        :param payback: expected return.
        :param risk: investment risk level (low: 0, medium: 1, high: 2)
        """

        self.id: int = id
        self.description: str = description
        self.cost: int = cost
        self.payback: int = payback
        self.risk: int = risk

    def __str__(self) -> str:
        return f"Investment Option {self.id}:\nDescription: {self.description}\nCost: {self.cost}\nPayback: {self.payback}\nRisk: {self.risk}\n"