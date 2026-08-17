from decimal import Decimal

from pydantic import BaseModel, Field, field_validator


class OperationRequest(BaseModel):
    wallet_name: str = Field(..., max_length=127)
    amount: Decimal
    description: str | None = Field(None, max_length=255)

    @field_validator("amount")
    def amount_must_be_positive(cls, value: Decimal) -> Decimal:
        # значение больше нуля
        if value <= 0:
            raise ValueError("Amount must be positive")
        # возвращаем значение если все ок
        return value

    @field_validator("wallet_name")
    def wallet_name_not_empty(cls, value: str) -> str:
        # убираем пробелы по краям
        value = value.strip()
        if not value:
            raise ValueError("Wallet name cannot be empty")
        return value


class CreateWalletRequest(BaseModel):
    name: str = Field(..., max_length=127)
    initial_balance: Decimal = 0

    @field_validator("name")
    def wallet_name_not_empty(cls, value: str) -> str:
        # убираем пробелы по краям
        value = value.strip()
        if not value:
            raise ValueError("Wallet name cannot be empty")
        return value

    @field_validator("initial_balance")
    def balance_not_negative(cls, value: Decimal) -> Decimal:
        # значение больше нуля
        if value <= 0:
            raise ValueError("initial_balance cannot negative")
        # возвращаем значение если все ок
        return value
