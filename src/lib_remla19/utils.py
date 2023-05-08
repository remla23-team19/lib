import pkg_resources

class VersionUtil:
    @staticmethod
    def get_version():
        try:
            version = pkg_resources.get_distribution("lib-remla19").version
        except pkg_resources.DistributionNotFound:
            version = "unknown"
        return version

