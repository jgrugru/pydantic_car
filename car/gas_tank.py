from typing import Callable, Generator, Dict, Any
from pydantic import (
    Field,
    BaseModel,
    confloat,
    StrictFloat,
    validator,
    condecimal,
    ConstrainedDecimal,
    ConstrainedFloat,
)


class Percent(float):
    """
    Float type that validates the float is a percent
    in the format of 0.0 <= x <= 1.00.
    """

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[[float], float], None, None]:
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        # __modify_schema__ should mutate the dict it receives in place,
        # the returned value will be ignored
        field_schema.update(pattern="0.0 <= x <= 1.00", type="float")

    @classmethod
    def validate(cls, v: float) -> float:
        if not isinstance(v, float):
            raise TypeError("float required")
        if not 0 <= v <= 1:
            raise TypeError(
                "Not a valid percent. Needs to be within 0.0 <= value <= 1.00"
            )
        return v

    def __repr__(self) -> str:
        return f"Percent({super().__repr__()})"


class GasTank(BaseModel):
    """The below commented out code shows how to make a percentage type
    that is used to represent the current level of the tank.
    There are 3 possible ways to do this in pydantic:
    - create your own class with validate and update_schema function.
      Class is created above.
    - use con (constrain) pydantic types
    - create own validator function using validator decorator"""

    capacity: int = Field(le=35, gt=0)

    # Confloat:
    # Very simple method to define percent. Down side it is not
    # reusable. Will have to define in multiple places.
    # fill: confloat(ge=0.0, le=1.0)

    # Condecimal:
    # A variant of the above version but with more constraints:
    # Now limits on the decimal places
    # fill: condecimal(ge=0.0, le=1.0, decimal_places=2)

    # class Percent:
    # Percent is it's own class and has it's own validate function.
    # Advantage of this is that it is reusable elsewhere as well as ability to
    # modify the schema, more control.
    fill: Percent

    # Validator:
    # Probably the worst choice in this case. Extra overhead and the
    # the code is not reuseable/modular. Limits transferability of model.
    # fill: StrictFloat = Field(default=1.0)
    # @validator("fill")
    # def fill_validator(cls, v):
    #     if not 0 <= v <= 1:
    #         raise TypeError('Not a valid float. Needs to be within 0.0 <= value <= 1.00')
    #     return v

    class Config:
        validate_arguments = True


# x = GasTank(capacity=15, fill=0.1)
# print(x.schema_json())
