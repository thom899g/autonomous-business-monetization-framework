from typing import Dict, Any
import logging

class SubscriptionManager:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
    
    def create_subscription(self, user_id: str, tier: str) -> bool:
        """Create a new subscription for the specified user tier."""
        try:
            # Validate tier against available plans
            if tier not in self.config['subscriptions']['tiered_plans']:
                raise ValueError("Invalid subscription tier")
            
            # Mock payment processing
            payment_gateway = PaymentGateway()
            response = payment_gateway.process_payment(user_id, tier)
            
            if response.status == 'success':
                self.logger.log_event(f"Subscription created for user {user_id} at tier {tier}", level='INFO')
                return True
            else:
                raise SubscriptionError("Payment processing failed")
                
        except Exception as e:
            self.logger.log_error(e)
            return False
    
    def apply_discount(self, subscription_id: str) -> float:
        """Apply discounts based on subscription tiers."""
        try:
            # Determine discount based on tier
            tier = self._get_subscription_tier(subscription_id)
            
            if tier == 'basic':
                discount = 0.1
            elif tier == 'pro':
                discount = 0.2
            else:
                discount = 0.3
                
            return round(self.config['subscriptions']['tiered_plans'][tier] * (1 - discount), 2)
            
        except Exception as e:
            raise DiscountError(f"Failed to apply discount: {str(e)}")