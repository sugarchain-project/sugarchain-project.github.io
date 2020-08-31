#! /usr/bin/env python3

from matplotlib import pyplot
from pathlib import Path
import pandas
import seaborn

THIS_FILE = Path(__file__)

# Benchmark measurements were taken from `cargo bench '16384$'` run in this
# directory and hardcoded here. The machine used was an AWS c5.metal instance,
# with an Intel Cascade Lake-SP 8275CL processor, running Arch Linux. MD5,
# SHA-1, SHA-2, and SHA-3 are all provided by OpenSSL. BLAKE2b and BLAKE2s are
# provided by the `blake2b_simd` and `blake2s_simd` crates. BLAKE3 is provided
# by the `blake3` crate.
#
# Note that while the benchmark machine supports AVX-512, the `blake2b_simd`
# and `blake2s_simd` crates do not currently include explicit AVX-512
# rotations. To get the compiler to include those rotations, I set the env var
# `RUSTFLAGS="-C target-cpu=native"`, for the BLAKE2 benchmarks only.
#
# Although the benchmark suite includes other parallel algorithms (BLAKE2bp,
# BLAKE2sp, KangarooTwelve), their figures are omitted here. That's both
# because they are uncommon -- for example, not supported in OpenSSL -- and
# also because the 16 KiB input length used here would be unfair to them.

BARS = [
    ("t1", 198),
    ("2", 387),
    ("3", 557),
    ("4", 714),
    ("5", 832),
    ("6", 899),
    ("7", 896),
    ("8", 920),
    ("9", 917),
    ("10", 955),
    ("11", 936),
    ("12", 924),
    ("13", 947),
    ("14", 955),
    ("15", 947),
    ("16", 939),
]


# adapted from https://stackoverflow.com/a/56780852/823869
def show_values_on_bars(axes):
    # left_padding = 100
    # left_padding = -1/1.75
    left_padding = -1/2.4
    bottom_padding = -0.25*7*7
    for p in axes.patches:
        _x = p.get_x() + p.get_width() + float(left_padding)
        _y = p.get_y() + p.get_height() - float(bottom_padding)
        # value = int(p.get_width())
        value = int(p.get_height())
        axes.text(_x, _y, value, ha="center")


def main():
    names = [x[0] for x in BARS]
    values = [x[1] for x in BARS]
    dataframe = pandas.DataFrame({"names": names, "values": values})
    seaborn.set()
    seaborn.set_style("ticks")
    # pyplot.rcParams["axes.labelsize"] = 20
    # pyplot.rcParams["pgf.rcfonts"] = False
    # pyplot.rcParams["font.family"] = "serif"
    pyplot.rcParams["font.family"] = "DejaVu Sans"
    pyplot.figure(figsize=[12, 6])
    # seaborn.set_context("paper")
    # seaborn.set_context("talk")
    plot = seaborn.barplot(
        data=dataframe,
        x="names",
        y="values",
        color="teal",
        edgecolor="black",
        # linewidth=3,
    )
    show_values_on_bars(plot.axes)
    plot.set_title("Multi-Threading Efficiency: YespowerSugar Performance\n CPU: Ryzen 1700(stock), RAM: DDR4 2400 MT/s\n Version=1.0.1 N=2048 r=32, Using 8192.00 KiB RAM")
    plot.set(xlabel="Threads Amount (t)")
    plot.set(ylabel="Hashrate (h/s)")
    pyplot.xlim(-1, 16)
    pyplot.ylim(0, 1100)
    # pyplot.savefig(THIS_FILE.with_suffix(".svg"), bbox_inches="tight")
    # pyplot.savefig(THIS_FILE.with_suffix(".png"), bbox_inches="tight")
    pyplot.show()


if __name__ == "__main__":
    main()
