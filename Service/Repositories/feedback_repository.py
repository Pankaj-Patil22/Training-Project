import json
from sqlite3 import Date
from flask import session
import Models.feedback as feedback_model
from Models.feedback import OverallFeedback, ItemFeedback
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind=feedback_model.engine))

class FeedbackRepository:
    
    @staticmethod
    def add_overall_feedback(order_id, rating, review):
        feedback = OverallFeedback(order_id, rating, review)
        session.add(feedback)
        session.commit()
        return feedback.id

    @staticmethod
    def add_item_feedback(feedback_id, item_id, rating, review):
        feedback = ItemFeedback(feedback_id, item_id, rating, review)
        session.add(feedback)
        session.commit()
        return feedback.id

    @staticmethod
    def get_feedback_for_order(order_id):
        feedback = session.query(OverallFeedback).filter(OverallFeedback.order_id == order_id).first()
        return feedback

    @staticmethod
    def get_feedback_by_id(feedback_id):
        feedback = session.query(OverallFeedback).filter(OverallFeedback.id == feedback_id).first()
        return feedback
    
    @staticmethod
    def get_items_feedback_by_feedback_id(overall_feedback_id):
        feedback = session.query(ItemFeedback).filter(ItemFeedback.feedback_id == overall_feedback_id).all()
        return feedback