# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=too-few-public-methods

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category
from factory import Faker
from service.common import db

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Product

    id = factory.Sequence(lambda n: n)
   ## Add code to create Fake Products 
    name = Faker("word")
    description = Faker("sentence")
    price = fuzzy.FuzzyDecimal(0.99, 999.99, 2)
    available = fuzzy.FuzzyChoice([True, False])
    category = fuzzy.FuzzyChoice(
        ["FOOD", "CLOTHING", "ELECTRONICS", "HOUSEWARES"]
    )

    @classmethod
    def create(cls, **kwargs):
        """Create and persist a product to the database"""
        product = cls.build(**kwargs)
        db.session.add(product)
        db.session.commit()
        return product
