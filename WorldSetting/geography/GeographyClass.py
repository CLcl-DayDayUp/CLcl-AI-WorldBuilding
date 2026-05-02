# utf-8
#
# ====================================================================
# @Author: CLcl
# @Date: 2026-5-02
# @Description: Geography class for handling geographical data and operations.
#               这是一个地理类，用于处理与地理相关的数据和操作,仅仅作为父类模板使用

# ====================================================================
from abc import ABC, abstractmethod
from boilogies.BoilogyClass import Biology


class Geography(ABC):
    """
    地理接口类（抽象基类）
    子类必须实现所有属性与方法
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """地理实体名称"""
        pass

    @property
    @abstractmethod
    def area(self) -> float:
        """面积 Km²"""
        pass

    @property
    @abstractmethod
    def direction_description(self) -> str:
        """方位描述"""
        pass

    @property
    @abstractmethod
    def climate(self) -> str:
        """气候"""
        pass

    @property
    @abstractmethod
    def main_species(self) -> list[Biology]:
        """主要生物"""
        pass

    @property
    @abstractmethod
    def political_entity(self) -> str:
        """政治实体"""
        pass

    @abstractmethod
    def get_info(self) -> str:
        """返回地理信息"""
        pass
