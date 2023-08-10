#!/usr/bin/python3
"""Contains unittests for module base_model"""
import unittest
from models import base_model
from models.base_model import BaseModel
from datetime import datetime

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

my_model2 = BaseModel()


class TestBaseModel(unittest.TestCase):
    """Unittests test cases for class BaseModel"""

    def testClassDocs(self):
        """Check if class docs are available"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def testModuleDocs(self):
        """Check if module docs are available"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def testClassMethodDocs(self):
        """Check if method docs are available"""
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)

    def testInstanceType(self):
        """Check if the type of object is BaseModel class"""
        self.assertTrue(type(my_model), BaseModel)

    def testBaseModelType(self):
        """Check if the type of BaseModel is object class"""
        self.assertTrue(type(BaseModel), object)

    def testUniqueId(self):
        """Check if each object gets a unique id from uuid"""
        self.assertNotEqual(my_model.id, my_model2.id)

    def testHasId(self):
        """Check if object has an id attribute"""
        self.assertTrue(my_model.id)

    def testHasCreatedAt(self):
        """Check if object has an created_at attribute"""
        self.assertTrue(my_model.created_at)

    def testHasUpdatedAt(self):
        """Check if object has an updated_at attribute"""
        self.assertTrue(my_model.updated_at)

    def testHasSave(self):
        """Check if object has method save()"""
        self.assertTrue(my_model.save)

    def testHasToDict(self):
        """Check if object has method to_dict()"""
        self.assertTrue(my_model.to_dict)

    def testHasStr(self):
        """Check if object has method __str__()"""
        self.assertTrue(my_model.__str__)

    def testManualAttributeName(self):
        """Check if object has the manual attribute 'name'"""
        self.assertTrue(my_model.name, "My First Model")

    def testManualAttributeMyNumber(self):
        """Check if object has the manual attribute 'my_number'"""
        self.assertTrue(my_model.my_number, 89)

    def testAfterSaveUpdatedAtChange(self):
        """Check if the updated_at attribute changes after save"""
        modl = BaseModel()
        modlBeforeSave = modl.updated_at
        modl.save()
        modlAfterSave = modl.updated_at
        self.assertNotEqual(modlBeforeSave, modlAfterSave)

    def testTypeReturnedFromToDict(self):
        """Check if to_dict() returns a dictionary"""
        myModelDict = my_model.to_dict()
        self.assertTrue(type(myModelDict), dict)

    def testDictClassAttributein(self):
        """Check __class__ attribute in object dict"""
        dModel = my_model.to_dict()
        self.assertTrue("__class__" in dModel.keys())

    def testCreatedAtISOFormatString(self):
        """Check if created_at time in dict is an ISO string"""
        dictModel = my_model.to_dict()
        self.assertTrue(type(dictModel["created_at"]), str)

    def testUpdatedAtISOFormatString(self):
        """Check if updated_at time in dict is an ISO string"""
        dictmodel = my_model.to_dict()
        self.assertTrue(type(dictmodel["updated_at"]), str)

    def testIfIDisString(self):
        """Check if object id in dict is a string"""
        dictmodelId = my_model.to_dict()
        self.assertTrue(type(dictmodelId["id"]), str)

    def testTypeOfCreatedAtDate(self):
        """Check the type of created_at date in object"""
        dictMod = my_model.__dict__
        self.assertTrue(type(dictMod["created_at"]), datetime)

    def testTypeOfUpdatedAtDate(self):
        """Check the type of updated_at date in object"""
        dictMod = my_model.__dict__
        self.assertTrue(type(dictMod["updated_at"]), datetime)

    def testKwargs(self):
        """Check kwargs can create an object model"""
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertTrue(my_new_model)

    def testSameIdObjects(self):
        """Check same id in object created with another object's dict"""
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)

    def testIfSameObject(self):
        """Check if object created with another object's dict
        is the same object as the source object"""
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertNotEqual(my_model, my_new_model)

    def testDictValueUsed(self):
        """Check if each dictionary value is the corresponding
        value of the attribute"""
        my_model = BaseModel()
        use_dict = {"name": "Another model", "number": 77}
        new_model = BaseModel(**use_dict)
        self.assertEqual(use_dict["number"], new_model.number)

    def testClassKwargNotAdded(self):
        """Check if kwarg __class__ is given, it's not added"""
        my_model = BaseModel()
        use_dict = {"__class__": "myClass", "number": 33}
        new_model = BaseModel(**use_dict)
        new_model_cls = new_model.__class__.__name__
        self.assertNotEqual(use_dict["__class__"], new_model_cls)

    def testFloatValueKwarg(self):
        """Test kwarg float value"""
        mod = BaseModel()
        aDict = {"player": "Dirk", "number": 4.1}
        nMod = BaseModel(**aDict)
        self.assertEqual(nMod.number, 4.1)

    def testNoneValueKwarg(self):
        """Test kwarg None value"""
        mod = BaseModel()
        aDict = {"player": "Dirk", "number": None}
        nMod = BaseModel(**aDict)
        self.assertEqual(nMod.number, None)

    def testEmptyStringValueKwarg(self):
        """Test empty string kwarg value"""
        mod = BaseModel()
        aDict = {"player": "", "number": None}
        nMod = BaseModel(**aDict)
        self.assertEqual(len(nMod.player), 0)

    def testBooleanValueKwarg(self):
        """Test boolean kwarg value"""
        mod = BaseModel()
        aDict = {"player": False, "number": 4.1}
        nMod = BaseModel(**aDict)
        self.assertEqual(nMod.player, False)

    def testListValueKwarg(self):
        """Test kwarg list value"""
        mod = BaseModel()
        pList = ["Dirk", "Curry", "Ball"]
        aDict = {"player": pList, "number": 4.1}
        nMod = BaseModel(**aDict)
        self.assertEqual(nMod.player, pList)

    def testTupleValueKwarg(self):
        """Test kwarg tuple value"""
        mod = BaseModel()
        pTuple = [30, 2, 0]
        aDict = {"player": "Kawhi", "jersey": pTuple}
        nMod = BaseModel(**aDict)
        self.assertEqual(nMod.jersey, pTuple)

    def testDictValueKwarg(self):
        """Test kwarg dictionary value"""
        mod = BaseModel()
        pDict = ["Klay", "Poole", "Young"]
        aDict = {"players": pDict, "jersey": 2}
        nMod = BaseModel(**aDict)
        self.assertEqual(nMod.players, pDict)

    def testNegativeIntKwarg(self):
        """Test kwarg negative int value"""
        mod = BaseModel()
        aDict = {"name": "Dirk", "jersey": -18}
        nMod = BaseModel(**aDict)
        self.assertEqual(nMod.jersey, -18)


if __name__ == "__main__":
    unittest.main()