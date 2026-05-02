# utf-8
#
# ====================================================================
# @Author: CLcl
# @Date: 2026-5-02
# @Description: Political class for handling political data and operations.
#               这是一个政治类，用于处理与政治相关的数据和操作,仅仅作为父类模板使用

# ====================================================================
from abc import ABC, abstractmethod
from boilogies.BoilogyClass import Biology
from geography.GeographyClass import Geography
from characters.CharacterClass import Character


class Polity(ABC):
    """
    政治实体类，用于处理与政治实体相关的数据和操作
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """政治实体名称"""
        pass

    @property
    @abstractmethod
    def geography(self) -> list[Geography]:
        """政治实体地理信息"""
        pass

    @property
    @abstractmethod
    def population(self) -> int:
        """政治实体人口"""
        pass

    @property
    @abstractmethod
    def area(self) -> float:
        """政治实体面积"""
        pass

    @property
    @abstractmethod
    def leaders(self) -> list[str]:
        """政治实体领导人"""
        pass

    @property
    @abstractmethod
    def laws(self) -> list[str]:
        """政治实体法律"""
        pass

    @property
    @abstractmethod
    def main_characters(self) -> list[Character]:
        """政治实体主要角色"""
        pass

    @property
    @abstractmethod
    def parent_polity(self) -> Polity:
        """政治实体所属政治实体"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """政治实体描述"""
        pass

    @abstractmethod
    def get_info(self) -> str:
        """返回政治实体信息"""
        pass
