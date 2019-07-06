import pytest
from pages.jqueryPage import DragNDrop


@pytest.mark.usefixtures("test_setup")
class TestDragNDrop:
    def test_dragndrop(self):
        driver = self.driver
        lp = DragNDrop(driver)
        lp.drag_n_drop()
