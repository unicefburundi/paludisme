# -*- coding: utf-8 -*-
from rest_framework import serializers
from stock.models import StockProduct, StockOutReport, Dosage, Report, CasesPalu, Tests
from bdiadmin.models import CDS, District, Province
from django.db.models import Sum
import datetime


class StockProductSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    dosage = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = StockProduct
        fields = ("product", "dosage", "quantity", "reporting_date", "category")

    def get_product(self, obj):
        return obj.product.designation

    def get_dosage(self, obj):
        return obj.dosage.dosage

    def get_category(self, obj):
        return obj.report.category


class StockProductProvSerializer(serializers.ModelSerializer):
    quantity_sf = serializers.SerializerMethodField()
    quantity_sd = serializers.SerializerMethodField()
    quantity_sr = serializers.SerializerMethodField()
    province = serializers.SerializerMethodField()

    class Meta:
        model = Province
        fields = ("id", "quantity_sf", "quantity_sd", "quantity_sr", "province", "code")

    def get_province(self, obj):
        return obj.name

    def get_quantity_sf(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility__district__province=obj, report__category="SF"
        )
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]

    def get_quantity_sd(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility__district__province=obj, report__category="SD"
        )
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]

    def get_quantity_sr(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility__district__province=obj, report__category="SR"
        )
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]


class StockProductDisSerializer(StockProductProvSerializer):
    district = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = (
            "id",
            "quantity_sf",
            "quantity_sd",
            "quantity_sr",
            "province",
            "district",
            "code",
        )

    def get_district(self, obj):
        return obj.name

    def get_province(self, obj):
        return obj.province.name

    def get_quantity_sf(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility__district=obj, report__category="SF"
        )
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]

    def get_quantity_sd(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility__district=obj, report__category="SD"
        )
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]

    def get_quantity_sr(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility__district=obj, report__category="SR"
        )
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]


class StockProductCDSSerializer(StockProductProvSerializer):
    cds = serializers.SerializerMethodField()

    class Meta:
        model = CDS
        fields = (
            "id",
            "quantity_sf",
            "quantity_sd",
            "quantity_sr",
            "province",
            "district",
            "cds",
            "code",
        )

    def get_cds(self, obj):
        return obj.name

    def get_district(self, obj):
        return obj.district.name

    def get_province(self, obj):
        return obj.district.province.name

    def get_quantity_sf(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility=obj, report__category="SF"
        )
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]

    def get_quantity_sd(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility=obj, report__category="SD"
        )
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]

    def get_quantity_sr(self, obj):
        queryset = StockProduct.objects.filter(
            report__facility=obj, report__category="SR"
        )
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        product = self.context["request"].GET.get("product", "")
        if product and product != "undefined":
            queryset = queryset.filter(product=product)
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(quantities=Sum("quantity"))["quantities"]


class StockOutProductSerializer(serializers.ModelSerializer):
    province = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    cds = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = StockOutReport
        fields = (
            "id",
            "province",
            "district",
            "cds",
            "product",
            "reporting_date",
            "remaining",
        )

    def get_province(self, obj):
        return obj.report.facility.district.province.name

    def get_district(self, obj):
        return obj.report.facility.district.name

    def get_cds(self, obj):
        return obj.report.facility.name

    def get_product(self, obj):
        return obj.product.designation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosage
        fields = ("id", "dosage", "rank")


class CasesPaluSerializer(serializers.Serializer):
    week = serializers.IntegerField()
    simple = serializers.IntegerField()
    acute = serializers.IntegerField()
    pregnant_women = serializers.IntegerField()
    decease = serializers.IntegerField()
    year = serializers.IntegerField()

    class Meta:
        fields = ("simple", "acute", "pregnant_women", "decease", "week", "year")


class CasesPaluProvSerializer(serializers.ModelSerializer):
    simple = serializers.SerializerMethodField()
    acute = serializers.SerializerMethodField()
    pregnant_women = serializers.SerializerMethodField()
    decease = serializers.SerializerMethodField()
    ge = serializers.SerializerMethodField()
    tdr = serializers.SerializerMethodField()
    province = serializers.SerializerMethodField()

    class Meta:
        model = Province
        fields = (
            "id",
            "simple",
            "acute",
            "pregnant_women",
            "decease",
            "ge",
            "tdr",
            "province",
            "code",
        )

    def get_province(self, obj):
        return obj.name

    def get_simple(self, obj):
        queryset = CasesPalu.objects.filter(report__facility__district__province=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(simples=Sum("simple"))["simples"]

    def get_acute(self, obj):
        queryset = CasesPalu.objects.filter(report__facility__district__province=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(acutes=Sum("acute"))["acutes"]

    def get_pregnant_women(self, obj):
        queryset = CasesPalu.objects.filter(report__facility__district__province=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(pregnant_womens=Sum("pregnant_women"))[
            "pregnant_womens"
        ]

    def get_decease(self, obj):
        queryset = CasesPalu.objects.filter(report__facility__district__province=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(deceases=Sum("decease"))["deceases"]

    def get_ge(self, obj):
        queryset = Tests.objects.filter(report__facility__district__province=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(ges=Sum("ge"))["ges"]

    def get_tdr(self, obj):
        queryset = Tests.objects.filter(report__facility__district__province=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(tdrs=Sum("tdr"))["tdrs"]


class CasesPaluDisSerializer(CasesPaluProvSerializer):
    province = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = (
            "id",
            "simple",
            "acute",
            "pregnant_women",
            "decease",
            "ge",
            "tdr",
            "province",
            "code",
            "district",
        )

    def get_province(self, obj):
        return obj.province.name

    def get_district(self, obj):
        return obj.name

    def get_simple(self, obj):
        queryset = CasesPalu.objects.filter(report__facility__district=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(simples=Sum("simple"))["simples"]

    def get_acute(self, obj):
        queryset = CasesPalu.objects.filter(report__facility__district=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(acutes=Sum("acute"))["acutes"]

    def get_pregnant_women(self, obj):
        queryset = CasesPalu.objects.filter(report__facility__district=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(pregnant_womens=Sum("pregnant_women"))[
            "pregnant_womens"
        ]

    def get_decease(self, obj):
        queryset = CasesPalu.objects.filter(report__facility__district=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(deceases=Sum("decease"))["deceases"]

    def get_ge(self, obj):
        queryset = Tests.objects.filter(report__facility__district=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(ges=Sum("ge"))["ges"]

    def get_tdr(self, obj):
        queryset = Tests.objects.filter(report__facility__district=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(tdrs=Sum("tdr"))["tdrs"]


class CasesPaluCdsSerializer(CasesPaluProvSerializer):
    province = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    cds = serializers.SerializerMethodField()

    class Meta:
        model = CDS
        fields = (
            "id",
            "simple",
            "acute",
            "pregnant_women",
            "decease",
            "ge",
            "tdr",
            "province",
            "code",
            "district",
            "cds",
        )

    def get_province(self, obj):
        return obj.district.province.name

    def get_district(self, obj):
        return obj.district.name

    def get_cds(self, obj):
        return obj.name

    def get_simple(self, obj):
        queryset = CasesPalu.objects.filter(report__facility=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(simples=Sum("simple"))["simples"]

    def get_acute(self, obj):
        queryset = CasesPalu.objects.filter(report__facility=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(acutes=Sum("acute"))["acutes"]

    def get_pregnant_women(self, obj):
        queryset = CasesPalu.objects.filter(report__facility=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(pregnant_womens=Sum("pregnant_women"))[
            "pregnant_womens"
        ]

    def get_decease(self, obj):
        queryset = CasesPalu.objects.filter(report__facility=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(deceases=Sum("decease"))["deceases"]

    def get_ge(self, obj):
        queryset = Tests.objects.filter(report__facility=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(ges=Sum("ge"))["ges"]

    def get_tdr(self, obj):
        queryset = Tests.objects.filter(report__facility=obj)
        startdate = self.context["request"].GET.get("startdate", "")
        enddate = self.context["request"].GET.get("enddate", "")
        if startdate and startdate != "undefined":
            queryset = queryset.filter(
                reporting_date__gte=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            )
        if enddate and enddate != "undefined":
            queryset = queryset.filter(
                reporting_date__lte=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            )
        return queryset.aggregate(tdrs=Sum("tdr"))["tdrs"]


class RateSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    week = serializers.IntegerField()
    nombre = serializers.IntegerField()
    expected = serializers.SerializerMethodField()

    def get_expected(self, obj):
        reports = (
            Report.objects.filter(
                category__in=["SF", "CA", "TS"],
                reporting_date__year=obj["year"],
                reporting_date__week=obj["week"],
            )
            .values("facility")
            .distinct()
            .count()
        )
        return reports * 7


class ReportSerializer(serializers.ModelSerializer):
    cds = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    province = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = (
            "id",
            "reporting_date",
            "province",
            "district",
            "cds",
            "text",
            "category",
        )

    def get_province(self, obj):
        return obj.facility.district.province.name

    def get_district(self, obj):
        return obj.facility.district.name

    def get_cds(self, obj):
        return obj.facility.name
