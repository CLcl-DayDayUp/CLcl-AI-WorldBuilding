# utf-8
#
# ====================================================================
# @Author: CLcl
# @Date: 2026-5-02
# @Description: Biology class for handling biological data and operations.
#               这是一个种族类，用于处理与种族相关的数据和操作,仅仅作为父类模板使用

# ====================================================================
from abc import ABC, abstractmethod
from geography.GeographyClass import Geography


class Biology(ABC):
    """种族类，用于处理与种族相关的数据和操作"""

    @property
    @abstractmethod
    def name(self) -> str:
        """种族名称"""
        pass

    @property
    @abstractmethod
    def habitat(self) -> list[Geography]:
        """栖息地 可以广泛分布在多个地理区域"""
        pass

    @property
    @abstractmethod
    def body_shape(self) -> str:
        """体型"""
        pass

    @property
    @abstractmethod
    def life_span(self) -> float:
        """寿命"""
        pass

    @property
    @abstractmethod
    def reproduction(self) -> str:
        """繁殖方式"""
        pass

    @property
    @abstractmethod
    def behavior(self) -> str:
        """行为习性"""
        pass

    @property
    @abstractmethod
    def is_intelligent(self) -> bool:
        """是否是智慧生物"""
        pass

    @property
    @abstractmethod
    def is_magical(self) -> bool:
        """是否是魔法生物"""
        pass

    @abstractmethod
    def get_info(self) -> str:
        """返回种族信息"""
        pass
