import os

import obsws_python as obs


def main() -> None:
    host = os.getenv("OBS_HOST", "127.0.0.1")
    port = int(os.getenv("OBS_PORT", "4455"))
    password = os.getenv("OBS_PASSWORD", "")

    with obs.ReqClient(host=host, port=port, password=password, timeout=3) as client:
        scene_list = client.get_scene_list()
        print(f"Connected to OBS at {host}:{port}")
        print(f"Current program scene: {scene_list.current_program_scene_name}")

        for scene in scene_list.scenes:
            scene_name = scene["sceneName"]
            print(f"\nScene: {scene_name}")

            scene_items = client.get_scene_item_list(scene_name)
            if not scene_items.scene_items:
                print("  (no sources)")
                continue

            for item in scene_items.scene_items:
                enabled = "visible" if item["sceneItemEnabled"] else "hidden"
                print(f"  - {item['sourceName']} ({enabled})")

                if item["sourceName"] == "Spotify":
                    print(item)


if __name__ == "__main__":
    main()
