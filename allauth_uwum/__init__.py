"""Current version of the UWUM provider."""

major, minor, patch, stage, revision = (1, 1, 0, 'final', 0)

__version__ = '%s.%s' % (major, minor)

if patch:
    __version__ += '.%s' % (patch)

if stage != 'final':
    stage_mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
    __version__ += '%s%s' % (stage_mapping[stage], revision)
