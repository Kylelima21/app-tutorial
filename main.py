import numpy as np

from waggle.plugin import Plugin
from waggle.data.vision import Camera


def compute_color_stats(image):
    # Compute per-channel mean, max, and min.
    return {
        "mean": np.mean(image, axis=(0, 1)),
        "max": np.max(image, axis=(0, 1)),
        "min": np.min(image, axis=(0, 1)),
        "median": np.median(image, axis=(0, 1)),
    }

'''
def main():
  with Plugin() as plugin:
    # open camera and take an image
    with Camera("file://example.jpg") as camera:
        image = camera.snapshot()

    # compute mean color
    mean_color = compute_mean_color(image.data)

    # print mean color
    print(mean_color)
    plugin.publish("color.mean.r", mean_color[0], timestamp=image.timestamp)
    plugin.publish("color.mean.g", mean_color[1], timestamp=image.timestamp)
    plugin.publish("color.mean.b", mean_color[2], timestamp=image.timestamp)


    # compute max color
    max_color = compute_max_color(image.data)

    # print max color
    print(max_color)
    plugin.publish("color.max.r", max_color[0], timestamp=image.timestamp)
    plugin.publish("color.max.g", max_color[1], timestamp=image.timestamp)
    plugin.publish("color.max.b", max_color[2], timestamp=image.timestamp)


    # compute min color
    min_color = compute_min_color(image.data)

    # print max color
    print(min_color)
    plugin.publish("color.min.r", min_color[0], timestamp=image.timestamp)
    plugin.publish("color.min.g", min_color[1], timestamp=image.timestamp)
    plugin.publish("color.min.b", min_color[2], timestamp=image.timestamp)
'''

def main():
    with Plugin() as plugin, Camera("file://example.jpg") as camera:
        image = camera.snapshot()

        stats = compute_color_stats(image.data)
        channels = ("r", "g", "b")

        for stat_name, values in stats.items():
            print(f"{stat_name}: {values}")

            for channel, value in zip(channels, values):
                plugin.publish(
                    f"color.{stat_name}.{channel}",
                    float(value),
                    timestamp=image.timestamp,
                )

if __name__ == "__main__":
    main()
