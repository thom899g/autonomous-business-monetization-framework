from typing import Dict, Any
import numpy as np

class DynamicPricingStrategy:
    def __init__(self, config):
        self.config = config
        self.models = {
            'time_series': TimeSeriesModel(),
            'machine_learning': MLModel()
        }
    
    def calculate_price(self, product_data: Dict[str, Any]) -> float:
        """Calculate dynamic price based on available models."""
        try:
            # Attempt machine learning model first
            ml_price = self.models['machine_learning'].predict(product_data)
            
            if np.isnan(ml_price):
                # Fallback to time series model
                ts_price = self.models['time_series'].predict(product_data)
                adjusted_price = max(
                    ts_price * (1 + self.config['pricing']['max_adjustment']),
                    self.config['pricing']['min_price']
                )
            else:
                adjusted_price = max(
                    ml_price * (1 + self.config['pricing']['max_adjustment']),
                    self.config['pricing']['min_price'],
                    min(ml_price * 2, self.config['pricing']['max_price'])
                )
            
            return round(adjusted_price, 2)
            
        except Exception as e:
            raise PricingError(f"Failed to calculate price: {str(e)}")