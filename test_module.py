import matplotlib as mpl
import sea_level_predictor


def test_draw_plot():
    fig = sea_level_predictor.draw_plot()
    assert isinstance(fig, mpl.figure.Figure)