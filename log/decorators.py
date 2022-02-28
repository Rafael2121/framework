import json
from .models import Log


def enable_logging(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        Log.objects.create(
            status=result.status_code,
            raw_content=json.dumps(result.data)
        )

        return result
    
    return wrapper
