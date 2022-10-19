import abc

class FeedbackService(abc.ABC):
    @abc.abstractclassmethod
    def get_items_in_order(self, order_id):
        pass

    def add_feedback(self, data):
        pass