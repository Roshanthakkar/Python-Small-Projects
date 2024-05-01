import time
from plyer import notification


if __name__ == "__main__":

    notification.notify(
        title="drink water minimum 1 glass",
        message=" its necessary for your health",

        # displaying time
        timeout=5
    )
    # waiting time
    time.sleep(60*60)
