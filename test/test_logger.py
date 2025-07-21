import logging
from utils.logger import get_logger

def test_get_logger_idempotent():
    name = "mi_logger"
    log1 = get_logger(name)
    log2 = get_logger(name)
    
    # Mismo objeto Logger y no duplica handlers
    assert log1 is log2
    assert len(log1.handlers) == len(log2.handlers)
    assert isinstance(log1, logging.Logger)
