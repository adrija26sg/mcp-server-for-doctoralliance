from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

sched = BackgroundScheduler()
sched.start()

def schedule_reminder(event_type: str, context: dict, delay: int = 60):
    from doctoralliance_agent.src.doctoralliance_agent.server import retrieve  # or import your dispatch wrapper
    run_at = datetime.now() + timedelta(seconds=delay)
    sched.add_job(lambda: retrieve({"event_type": event_type}),
                  trigger="date", run_date=run_at)
    return {"scheduled_at": run_at.isoformat()}
