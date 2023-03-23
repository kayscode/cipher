import time
import datetime


class Timer:
    def __init__(self, duration_in_seconds):
        self.start_date_time = datetime.datetime.now()
        self.end_date_time = self.start_date_time + datetime.timedelta(seconds=duration_in_seconds)
        self.result = None

    def start_timer(self, password: str, operation: callable):
        iteration = 0
        while True:
            current_loop_time = datetime.datetime.now()

            if current_loop_time >= self.end_date_time:
                break
            else:
                generated_password = operation()
                if generated_password == password:
                    return {"message": " password is weak", "is_password_strong": False, "password": password,
                            "generated_pass": generated_password}
                print(f" test {iteration} password: {password}, generated_password:{generated_password}")
                iteration += 1

        return {"message": "password is strong", "is_password_strong": True}
