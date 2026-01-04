# -*- coding: utf-8 -*-
"""
开发：Excellent（11964948@qq.com）
功能：设计系统模块 - 超越 UI UX Pro Max
作用：生成完整的设计系统、美学方向、design tokens、Landing 模式、图表推荐、UX 指南
创建时间：2025-12-30
最后修改：2025-01-04
"""

from .engine import DesignIntelligenceEngine, EnhancedBM25
from .generator import DesignSystemGenerator, DesignSystem
from .aesthetics import AestheticEngine, AestheticDirection, AestheticDirectionType
from .tokens import TokenGenerator
from .landing import LandingPatternGenerator, LandingPattern, CTAStrategy, get_landing_generator
from .charts import ChartRecommender, ChartType, ChartRecommendation, get_chart_recommender
from .ux_guide import UXGuideEngine, UXGuideline, UXRecommendation, get_ux_guide

__all__ = [
    "DesignIntelligenceEngine",
    "EnhancedBM25",
    "DesignSystemGenerator",
    "DesignSystem",
    "AestheticEngine",
    "AestheticDirection",
    "AestheticDirectionType",
    "TokenGenerator",
    "LandingPatternGenerator",
    "LandingPattern",
    "CTAStrategy",
    "get_landing_generator",
    "ChartRecommender",
    "ChartType",
    "ChartRecommendation",
    "get_chart_recommender",
    "UXGuideEngine",
    "UXGuideline",
    "UXRecommendation",
    "get_ux_guide",
]
