import subprocess

class P5:
    def __init__(self):
        pass
    def run_sketch(self, sketchname):
        path = f"java -jar processing_handler\processingpy\processing-py.jar  processing_handler\processing_sketches\{sketchname}.py"
        try:
            res = subprocess.check_output(path.split())
            return res
        except OSError as e:
            return e
        except subprocess.CalledProcessError as e:
            return e


if __name__ == "__main__":
    run = P5()
    run.run_sketch("template_letters")
