from pathlib import Path

class DemoBackend:
    def describe(self, image: Path) -> str:
        return f"outdoor observation from {image.name}"

class GemmaBackend:
    def __init__(self, runtime):
        self.runtime = runtime

    def describe(self, image: Path) -> str:
        return self.runtime.describe_image(str(image))
