import yaml
import random
import subprocess
import time
import os
from datetime import datetime
from pathlib import Path

from utils.logger import setup_logger

logger = setup_logger()

CONFIG_PATH = Path("config/settings.yaml")
PATHS_PATH = Path("config/paths.yaml")
ROLES_DIR = Path("roles")


def load_yaml(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_config():
    settings = load_yaml(CONFIG_PATH)
    paths = load_yaml(PATHS_PATH)
    role_name = settings["role"]
    role_file = ROLES_DIR / f"{role_name}.yaml"
    role = load_yaml(role_file)
    return settings, paths, role


def weighted_choice(activities):
    weights = [a.get("weight", 1) for a in activities]
    return random.choices(activities, weights=weights, k=1)[0]


def run_action(action, paths):
    action_type = action["action"]

    if action_type == "open_app":
        app_name = action["app"]
        path = paths["apps"].get(app_name)
        if path:
            logger.info(f"Запуск приложения: {path}")
            subprocess.Popen([path], shell=True)
        else:
            logger.warning(f"Неизвестное приложение: {app_name}")

    elif action_type == "open_browser":
        urls = action["urls"]
        url = random.choice(urls)
        logger.info(f"Открытие браузера по ссылке: {url}")
        subprocess.Popen(["start", "", url], shell=True)

    elif action_type == "run_terminal_command":
        terminal = action["terminal"]
        command = action["command"]
        term_path = paths["apps"].get(terminal)
        if term_path:
            logger.info(f"Выполнение команды в {terminal}: {command}")
            subprocess.Popen([term_path, "/c", command], shell=True)
        else:
            logger.warning(f"Неизвестный терминал: {terminal}")

    elif action_type == "edit_file":
        path = os.path.expandvars(action["path"])
        logger.info(f"Открытие файла: {path}")
        subprocess.Popen(["start", "", path], shell=True)

    elif action_type == "sleep":
        seconds = action.get("seconds", 60)
        logger.info(f"Пауза на {seconds} секунд")
        time.sleep(seconds)

    else:
        logger.error(f"Неизвестное действие: {action_type}")


def is_work_time(settings):
    now = datetime.now()
    weekday = now.isoweekday()
    current_time = now.time()
    work_days = settings["work_days"]
    start = datetime.strptime(settings["work_start"], "%H:%M").time()
    end = datetime.strptime(settings["work_end"], "%H:%M").time()
    return weekday in work_days and start <= current_time <= end


def main():
    settings, paths, role = load_config()
    activities = role["activities"]

    logger.info("Агент LISA запущен под Windows")

    while True:
        if is_work_time(settings):
            activity = weighted_choice(activities)
            run_action(activity, paths)

            interval = random.randint(
                settings["activity_interval_min"],
                settings["activity_interval_max"]
            )
            logger.info(f"Следующее действие через {interval} секунд")
            time.sleep(interval)
        else:
            logger.info("Вне рабочего времени. Пауза 5 минут")
            time.sleep(300)


if __name__ == "__main__":
    main()
