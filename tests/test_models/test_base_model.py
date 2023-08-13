#!/usr/bin/python3
"""Contains unittests for module base_model"""
import unittest
from models import base_model
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
from models import storage

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

    def test_4_instantiation(self):
        """Generic alx object creation test"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def testObjectCreation(self):
        """Check object creation"""
        self.a_model = BaseModel()

    def testDocs2(self):
        """Checking method docs"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def testSaveMethod2(self):
        """Checking and testing save method"""
        self.bmodl = BaseModel()
        self.bmodl.save()
        self.assertTrue(hasattr(self.bmodl, "created_at"))

    def testDict(self):
        """Checking other attributes from object's dict"""
        bm = BaseModel()
        bmDict = bm.to_dict()
        self.assertEqual(bm.__class__.__name__, 'BaseModel')
        self.assertIsInstance(bmDict['updated_at'], str)
        self.assertIsInstance(bmDict['created_at'], str)

    def testOveriddenStrMethod(self):
        """Test __str__"""
        self.bm = BaseModel()
        bmCls = self.bm.__class__.__name__
        bmId = str(self.bm.id)
        bmDict = self.bm.__dict__
        stg = f"[{bmCls}] ({bmId}) {bmDict}"
        self.assertEqual(print(stg), print(self.bm))

    def testattr(self):
        """Test all attributes"""
        self.mod = BaseModel()
        self.assertTrue(hasattr(self.mod, "updated_at"))
        self.assertTrue(hasattr(self.mod, "created_at"))
        self.assertFalse(hasattr(self.mod, "hills"))
        self.assertFalse(hasattr(self.mod, "name"))
        self.assertTrue(hasattr(self.mod, "id"))
        self.mod.age = "74"
        self.mod.name = "Keanu"
        self.assertTrue(hasattr(self.mod, "name"))
        self.assertTrue(hasattr(self.mod, "age"))
        delattr(self.mod, "name")
        self.assertFalse(hasattr(self.mod, "name"))
        delattr(self.mod, "age")
        self.assertFalse(hasattr(self.mod, "age"))
        self.assertEqual(self.mod.__class__.__name__, "BaseModel")

    def testSave3(self):
        """ Testing save method again """
        self.model3 = BaseModel()
        self.model3.save()
        key = f"{self.model3.__class__.__name__}.{self.model3.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], self.model3)

    def testStr3(self):
        """ Testing str method again"""
        self.model3 = BaseModel()
        self.assertEqual(
            str(self.model3),
            f"[BaseModel] ({self.model3.id}) {self.model3.__dict__}"
        )

    def testIDPrinted(self):
        """Checking printing model id"""
        myMod = BaseModel()
        print(myMod.id)
        print(myMod)

    def testAlxToDict2(self):
        """Test alx to_dict"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".
                  format(key, type(my_model_json[key]), my_model_json[key]))

    def test_init_base_model_dict(self):
        """Test froom dict alx case"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        print(my_model.id)
        print(my_model)
        print(type(my_model.created_at))
        print("--")
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".
                  format(key, type(my_model_json[key]), my_model_json[key]))
        print("--")
        my_new_model = BaseModel(**my_model_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))
        print("--")
        print(my_model is my_new_model)

    def testObjectStored(self):
        """Test stored object"""
        self.assertIn(BaseModel(), storage.all().values())

    def testUnequalObjectIDs(self):
        """Test unequal instance ids"""
        mod1 = BaseModel()
        mod2 = BaseModel()
        self.assertNotEqual(mod1.id, mod2.id)

    def testDifferentCreationTimes(self):
        """Test different times"""
        md1 = BaseModel()
        sleep(0.08)
        md2 = BaseModel()
        self.assertLess(md1.created_at, md2.created_at)

    def testDictAttributes(self):
        """Test Dict Attributes"""
        md9 = BaseModel()
        md9.name = "Holberton"
        md9.my_number = 98
        self.assertIn("name", md9.to_dict())
        self.assertIn("my_number", md9.to_dict())

    def testDifferentTimesUpdated(self):
        """Test different times"""
        md1 = BaseModel()
        sleep(0.07)
        md2 = BaseModel()
        self.assertLess(md1.created_at, md2.created_at)

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test more datetimes"""
        mdd = BaseModel()
        mDict = mdd.to_dict()
        self.assertEqual(type(mDict["created_at"]), str)
        self.assertEqual(type(mDict["updated_at"]), str)

    def testNoneKwargs(self):
        """Test error None kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def testArgsKwargs(self):
        """Test using args and kwargs"""
        td = datetime.today()
        tdISO = td.isoformat()
        md = BaseModel(
            "12",
            id="345",
            created_at=tdISO,
            updated_at=tdISO
        )
        self.assertEqual(md.id, "345")
        self.assertEqual(md.created_at, td)
        self.assertEqual(md.updated_at, td)

    def test_contrast_to_dict_dunder_dict(self):
        """Test dict"""
        mdd = BaseModel()
        self.assertNotEqual(mdd.to_dict(), mdd.__dict__)

    def testOutputToDict(self):
        """Test output to_dict"""
        tdy = datetime.today()
        md = BaseModel()
        md.id = "123456"
        md.created_at = md.updated_at = tdy
        mdDict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': tdy.isoformat(),
            'updated_at': tdy.isoformat()
        }
        self.assertDictEqual(md.to_dict(), mdDict)

    def testFileSaves(self):
        """Test more on file save"""
        md3 = BaseModel()
        md3.save()
        mID = "BaseModel." + md3.id
        with open("file.json", "r") as rf:
            self.assertIn(mID, rf.read())

    def testCorrectKeys(self):
        """Test correct keys"""
        md5 = BaseModel()
        self.assertIn("id", md5.to_dict())
        self.assertIn("created_at", md5.to_dict())
        self.assertIn("updated_at", md5.to_dict())
        self.assertIn("__class__", md5.to_dict())

    def testNoneargToDict(self):
        """Test None arg to dict"""
        mdd = BaseModel()
        with self.assertRaises(TypeError):
            mdd.to_dict(None)


if __name__ == "__main__":
    unittest.main()
