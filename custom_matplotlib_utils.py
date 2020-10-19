import matplotlib.ticker as ticker
import matplotlib.scale as mscale
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np


class PrecisionDateFormatter(ticker.Formatter):
    """
    Extend the `matplotlib.ticker.Formatter` class to allow for millisecond
    precision when formatting a tick (in days since the epoch) with a
    `~datetime.datetime.strftime` format string.
    https://stackoverflow.com/questions/11107748/showing-milliseconds-in-matplotlib

    Example
        ax.xaxis.set_major_formatter(PrecisionDateFormatter("%H:%M:%S.{ms}"))
    """

    def __init__(self, fmt, precision=3, tz=None):
        """
        Parameters
        ----------
        fmt : str
            `~datetime.datetime.strftime` format string.
        """
        from matplotlib.dates import num2date
        if tz is None:
            from matplotlib.dates import _get_rc_timezone
            tz = _get_rc_timezone()
        self.num2date = num2date
        self.fmt = fmt
        self.tz = tz
        self.precision = precision

    def __call__(self, x, pos=0):
        if x == 0:
            raise ValueError("DateFormatter found a value of x=0, which is "
                             "an illegal date; this usually occurs because "
                             "you have not informed the axis that it is "
                             "plotting dates, e.g., with ax.xaxis_date()")

        dt = self.num2date(x, self.tz)
        ms = dt.strftime("%f")[:self.precision]

        return dt.strftime(self.fmt).format(ms=ms)

    def set_tzinfo(self, tz):
        self.tz = tz


class SquareRootScale(mscale.ScaleBase):
    """
    ScaleBase class for generating square root scale.
    https://stackoverflow.com/questions/42277989/square-root-scale-using-matplotlib-python

    Examples:
        fig, ax = plt.subplots(1)

        ax.plot(np.arange(0, 9)**2, label='$y=x^2$')
        ax.legend()

        ax.set_yscale('squareroot')
        ax.set_yticks(np.arange(0,9,2)**2)
        ax.set_yticks(np.arange(0,8.5,0.5)**2, minor=True)

        plt.show()
    """

    name = 'squareroot'

    def __init__(self, axis, **kwargs):
        # note in older versions of matplotlib (<3.1), this worked fine.
        # mscale.ScaleBase.__init__(self)

        # In newer versions (>=3.1), you also need to pass in `axis` as an arg
        mscale.ScaleBase.__init__(self, axis)

    def set_default_locators_and_formatters(self, axis):
        axis.set_major_locator(ticker.AutoLocator())
        axis.set_major_formatter(ticker.ScalarFormatter())
        axis.set_minor_locator(ticker.NullLocator())
        axis.set_minor_formatter(ticker.NullFormatter())

    def limit_range_for_scale(self, vmin, vmax, minpos):
        return max(0., vmin), vmax

    class SquareRootTransform(mtransforms.Transform):
        input_dims = 1
        output_dims = 1
        is_separable = True

        def transform_non_affine(self, a):
            return np.array(a)**0.5

        def inverted(self):
            return SquareRootScale.InvertedSquareRootTransform()

    class InvertedSquareRootTransform(mtransforms.Transform):
        input_dims = 1
        output_dims = 1
        is_separable = True

        def transform(self, a):
            return np.array(a)**2

        def inverted(self):
            return SquareRootScale.SquareRootTransform()

    def get_transform(self):
        return self.SquareRootTransform()


mscale.register_scale(SquareRootScale)

if __name__ == "__main__":
    ####### square scale ############
    fig, ax = plt.subplots(1)

    ax.plot(np.arange(0, 9)**2, label='$y=x^2$')
    ax.legend()

    ax.set_yscale('squareroot')
    ax.set_yticks(np.arange(0, 9, 2)**2)
    ax.set_yticks(np.arange(0, 8.5, 0.5)**2)

    plt.show()
