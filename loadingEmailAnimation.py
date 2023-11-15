import time
def loading_animation(duration):
    steps = 20
    step_time = duration / steps

    for i in range(steps):
        time.sleep(step_time)
        print("\r=> Sending email to attacker: [{:<20}] {:.1f}%".format("=" * (i + 1), ((i + 1) / steps) * 100), end="", flush=True)

    print("\nEmail sent successfully")