from pathlib import Path
from fetch_nasa_epic_images import fetch_nasa_epic_launch
from fetch_spacex_images import fetch_spacex_last_launch
from fetch_nasa_images import fetch_nasa_last_launch


if __name__ == '__main__':
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
    fetch_nasa_last_launch()
    fetch_nasa_epic_launch()
