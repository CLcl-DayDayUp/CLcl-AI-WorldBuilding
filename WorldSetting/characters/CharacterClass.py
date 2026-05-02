# utf-8
#
# ====================================================================
# @Author: CLcl
# @Date: 2026-5-02
# @Description: Character class for handling character-related data and operations.
#               这是一个角色类，用于处理与角色相关的数据和操作,仅仅作为父类模板使用

# ====================================================================

from abc import ABC, abstractmethod
from boilogies.BoilogyClass import Biology
from geography.GeographyClass import Geography
from polities.PoliticalClass import Polity


class Character(ABC):
    """
    角色类，用于处理与角色相关的数据和操作
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """角色名称"""
        pass

    @property
    @abstractmethod
    def age(self) -> int:
        """角色年龄"""
        pass

    @property
    @abstractmethod
    def gender(self) -> str:
        """角色性别"""
        pass

    @property
    @abstractmethod
    def species(self) -> Biology:
        """角色种族"""
        pass

    @property
    @abstractmethod
    def polity(self) -> Polity:
        """角色所属政治实体"""
        pass

    @property
    @abstractmethod
    def backstory(self) -> str:
        """角色背景故事"""
        pass

    @property
    @abstractmethod
    def skills(self) -> list[str]:
        """角色技能"""
        pass

    @abstractmethod
    def get_info(self) -> str:
        """返回角色信息"""
        pass
