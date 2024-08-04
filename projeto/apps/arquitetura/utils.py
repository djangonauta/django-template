import datetime

import arrow


class DataUtils:

    @classmethod
    def intervalo_dias(cls, inicio: datetime.date, fim: datetime.date) -> datetime.date:
        inicial = arrow.get(datetime.datetime.combine(inicio, datetime.time.min))
        final = arrow.get(datetime.datetime.combine(fim, datetime.time.min))
        return map(lambda d: d.date(), arrow.Arrow.range('day', inicial, final))

    @classmethod
    def total_dias_uteis(cls, inicio: datetime.date, fim: datetime.date) -> int:
        dias_uteis = list(range(5))  # 0 = segunda, 4 = sexta
        return sum(1 for d in cls.intervalo_dias(inicio, fim) if d.weekday() in dias_uteis)
