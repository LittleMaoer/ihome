
from django.db import models


class BaseModel(models.Model):
    # 定义基础的模型
    create_time = models.DateTimeField(null=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):

    phone = models.CharField(max_length=11, unique=True)  # 手机号
    pwd_hash = models.CharField(max_length=200)   # 密码
    name = models.CharField(max_length=30)   # 姓名
    avatar = models.ImageField(null=True, upload_to='upload')  # 头像
    id_name = models.CharField(max_length=30)  # 实名认证的姓名
    id_card = models.CharField(max_length=30)  # 实名认证的身份证号码

    class Meta:
        db_table = 'ihome_user'


class Area(BaseModel):
    """城区"""

    name = models.CharField(max_length=32, null=False)  # 区域名字
    # houses = models.relationship("House", backref="area")  # 区域的房屋

    class Meta:
        db_table = 'ihome_area'


    # def to_dict(self):
    #     return {
    #         'id':self.id,
    #         'name':self.name
    #     }


class House(BaseModel):
    """房屋信息"""

    # 房屋主人的用户编号
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    # 归属地的区域编号
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=64, null=False)  # 标题
    price = models.IntegerField(default=0)  # 单价，单位：分
    address = models.CharField(max_length=512, default="")  # 地址
    room_count = models.IntegerField(default=1)  # 房间数目
    acreage = models.CharField(max_length=64, default=0)  # 房屋面积
    unit = models.IntegerField(default="")  # 房屋单元， 如几室几厅
    capacity = models.IntegerField(default=1)  # 房屋容纳的人数
    beds = models.CharField(max_length=64, default="")  # 房屋床铺的配置
    deposit = models.IntegerField(default=0)  # 房屋押金
    min_days = models.IntegerField(default=1)  # 最少入住天数
    max_days = models.IntegerField(default=0)  # 最多入住天数，0表示不限制
    order_count = models.IntegerField(default=0)  # 预订完成的该房屋的订单数
    index_image_url = models.CharField(max_length=256, default="")  # 房屋主图片的路径
    facilities = models.ManyToManyField('Facility')

    class Meta:
        db_table = 'ihome_house'

    # def to_dict(self):
    #     return {
    #         'id':self.id,
    #         'title':self.title,
    #         'image': self.index_image_url if self.index_image_url else '',
    #         'area':self.area.name,
    #         'price':self.price,
    #         'create_time':self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
    #         'create_time':self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
    #         'room':self.room_count,
    #         'order_count':self.order_count,
    #         'address':self.address
    #     }
    #
    # def to_full_dict(self):
    #     return {
    #         'id':self.id,
    #         'user_avatar':self.user.avatar if self.user.avatar else '',
    #         'user_name':self.user.name,
    #         'title': self.title,
    #         'price':self.price,
    #         'address':self.area.name+self.address,
    #         'room_count':self.room_count,
    #         'acreage':self.acreage,
    #         'unit':self.unit,
    #         'capacity':self.capacity,
    #         'beds':self.beds,
    #         'deposit':self.deposit,
    #         'min_days':self.min_days,
    #         'max_days':self.max_days,
    #         'order_count':self.order_count,
    #         'images':[image.url for image in self.images],
    #         'facilities':[facility.to_dict() for facility in self.facilities],
    #     }


class HouseImage(BaseModel):
    """房屋图片"""

    # 房屋编号
    house_id = models.ForeignKey(House, on_delete=models.CASCADE, null=False)
    url = models.CharField(max_length=256, null=False)  # 图片的路径

    class Meta:
        db_table = 'ihome_house_image'


class Facility(BaseModel):
    """设施信息, 房间规格等信息"""

    name = models.CharField(max_length=32, null=False)  # 设施名字
    css = models.ImageField(null=True, upload_to='upload')  # 设施展示的图标

    class Meta:
        db_table = 'ihome_facility'
    #
    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'css': self.css
    #     }
    #
    # def to_house_dict(self):
    #     return {'id': self.id}


class Order(BaseModel):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    house_id = models.ForeignKey(House, on_delete=models.CASCADE, null=False)
    begin_date = models.DateTimeField(null=False)  # 入住时间
    end_date = models.DateTimeField(null=False)  # 离店时间
    days = models.IntegerField(null=False)  # 住多少天
    house_price = models.DecimalField(max_digits=7, decimal_places=2, null=False)  # 房间价格
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False)  # 总价格

    class Meta:
        db_table = 'ihome_order'

    # def to_dict(self):
    #     return {
    #         'order_id':self.id,
    #         'house_title':self.house.title,
    #         'image':self.house.index_image_url if self.house.index_image_url else '',
    #         'create_date':self.create_time.strftime('%Y-%m-%d'),
    #         'begin_date':self.begin_date.strftime('%Y-%m-%d'),
    #         'end_date':self.end_date.strftime('%Y-%m-%d'),
    #         'amount':self.amount,
    #         'days':self.days,
    #         'status':self.status,
    #         'comment':self.comment
    #