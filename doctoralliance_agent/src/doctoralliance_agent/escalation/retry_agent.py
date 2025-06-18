from .reminder_scheduler import schedule_reminder

class RetryAgent:
    MAX = 3
    def __init__(self):
        self.attempts = {}

    def retry(self, event_type: str, context: dict):
        cnt = self.attempts.get(event_type, 0)
        if cnt >= self.MAX:
            return {"error":"max retries reached"}
        self.attempts[event_type] = cnt+1
        delay = 60 * (2**cnt)
        return schedule_reminder(event_type, context, delay)
