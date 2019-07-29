import json
import jsonpath
from urllib import request
import string


data= {
    "retcode":"0",
    "errmsg":"",
    "data": {
        "searchm":{
            "Head":{
                "Query":{
                    "HcCid1s": "",
                    "HcCid2s": "",
                    "HcCid3s": "",
                    "QueryProcessor":{
                        "ExpandQueryStatus" : "",
                        "ExpandQuery" : ""
                    },
                    "Sort":{
                        "is_pop_brand_alternate_on":""
                    }
                },
                "Summary": {
                    "OrgSkuCount": "202",
                    "Page": {
                        "PageCount": "6",
                        "PageIndex": "1",
                        "PageSize": "40"
                    },
                    "ResultCount": "202",
                    "ResultCut": "0"
                }
            },
            "ObjA_Price":[

            {
                "max":3600,
                "min":0
            },

            {
                "max":4300,
                "min":3600
            },

            {
                "max":5000,
                "min":4300
            },

            {
                "max":6200,
                "min":5000
            },

            {
                "max":7400,
                "min":6200
            },

            {
                "max":8500,
                "min":7400
            },

            {
                "max":85000,
                "min":8500
            }

            ],
            "ObjB_TextCollection":{
                "brand":{
                    "id":"",
                    "pinyin":"",
                    "value":""
                },
                "exp_color":{
                    "value":""
                },
                "exp_size":{
                    "value":""
                }
            },
            "Paragraph": [

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/60957/3/4538/83251/5d2bd6efE4cf260f6/75f68103acd2d14e.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）抽油烟机灶具套装 家用吸油烟机燃气灶排烟灶套装 27A3+56B0（天然气）",
                        "CustomAttrList" : "侧吸式^排风量19(m3\x2Fmin)^智能感应",
                        "shortWarename" : "老板（Robam） 27A3烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "87062",
                    "dredisprice": "4399.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435458",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4369996",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t16372/117/1916350991/36263/f7b73036/5a694611N9ae106f5.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）侧吸式油烟机家用抽油烟机 吸油烟机 大吸力免拆洗 一键爆炒 CXW-200-26A5S",
                        "CustomAttrList" : "侧吸式^排风量19(m3\x2Fmin)^触控控制",
                        "shortWarename" : "老板（Robam） 26A5S油烟机"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "31604",
                    "dredisprice": "2380.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272637952",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4903580",
                    "property_flag": "0",
                    "flags": "4722816"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1906/246/1227921793/54496/456c9656/56886df5Nb3a10073.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）欧式油烟机家用抽油烟机 吸油烟机大吸力 免拆洗 CXW-200-8325",
                        "CustomAttrList" : "欧式^排风量17(m3\x2Fmin)^触控控制",
                        "shortWarename" : "老板（Robam） 8325油烟机"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "78669",
                    "dredisprice": "2099.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272637952",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "2297165",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t27169/188/97793067/128888/ee3f0f9c/5b84a796Nf9507bb0.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）燃气灶 嵌入式煤气灶具 家用双灶具嵌可用 天然气 JZ(Y\x2FT\x2FR)-56B0",
                        "CustomAttrList" : "天然气12T^钢化玻璃^1级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "219052",
                    "dredisprice": "1599.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272637952",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4297390",
                    "property_flag": "0",
                    "flags": "4722816"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/38341/36/7554/174832/5cec8ea3E36ad6b86/4f78d2c9055a20ca.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）魔厨MAX 侧吸式抽油烟机燃气灶具套装27A3H+37B2（天然气）",
                        "CustomAttrList" : "侧吸式^排风量20(m3\x2Fmin)及以上^大尺寸",
                        "shortWarename" : "老板（Robam） 27A3H烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "18324",
                    "dredisprice": "4999.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443650",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100000113335",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/83086/3/571/182147/5cec8fd7E7f18a235/6d194da285ce76c3.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）欧式抽油烟机灶具套装 家用吸油烟机燃气灶排烟灶套装67A1H+56B0（天然气）",
                        "CustomAttrList" : "欧式^排风量20(m3\x2Fmin)及以上^一级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "7137",
                    "dredisprice": "4199.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268460034",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100004410344",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/24885/23/5301/193987/5c3bf917E2e643b2f/e196d765ab86ae10.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）燃气灶 嵌入式煤气灶具 家用双灶具嵌可用天然气 聚中劲火（天然气）JZT-33B7",
                        "CustomAttrList" : "天然气12T^钢化玻璃^2级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "129215",
                    "dredisprice": "1199.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272629760",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "1044052",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/38571/40/6323/180550/5cd0f825E135a8803/1f149df2f8ed96c5.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）大吸力 免拆洗触控侧吸式抽油烟机燃气灶具套装26A5S+56B0（天然气）",
                        "CustomAttrList" : "侧吸式^排风量19(m3\x2Fmin)^一级能效",
                        "shortWarename" : "老板（Robam） 26A5S烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "69220",
                    "dredisprice": "3999.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435458",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4903502",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t20641/341/2059355309/91892/413b044c/5b447d54N75730e4f.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）大吸力 免拆洗触控欧式抽油烟机燃气灶具套装8325+32B2（天然气）",
                        "CustomAttrList" : "欧式^排风量17(m3\x2Fmin)^触控控制",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "28001",
                    "dredisprice": "3199.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435456",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "1717383",
                    "property_flag": "0",
                    "flags": "4722816"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t19987/321/1929491251/106966/1173099c/5b2c51d1N3c957787.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）中式家用小尺寸专用大吸力抽吸油烟机单机CXW-185-3009",
                        "CustomAttrList" : "中式^排风量16(m3\x2Fmin)^一级能效",
                        "shortWarename" : "老板（Robam） 3009"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "11707",
                    "dredisprice": "1299.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443648",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "8024545",
                    "property_flag": "0",
                    "flags": "4722816"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/9249/4/9463/134932/5c18577dEf679d5a2/42a29cd5169ded0e.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam)消毒柜 消毒嵌入式厨房碗柜家用 茶杯碗筷消毒  100升 五重净化 ZTD100B-727",
                        "CustomAttrList" : "嵌入式^81-100L^紫外线消毒",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1301",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "34644",
                    "dredisprice": "1789.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443648",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "3247835",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t20782/14/2643595550/102251/95952bd4/5b601f88N3e4ab595.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam） 大吸力免拆洗侧吸式 抽油烟机灶具套装（天然气）21A5+32B2",
                        "CustomAttrList" : "侧吸式^排风量17(m3\x2Fmin)^一级能效",
                        "shortWarename" : "老板（Robam） 21A5烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "18966",
                    "dredisprice": "3199.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435456",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4800757",
                    "property_flag": "0",
                    "flags": "4722816"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t6727/336/434950377/40232/4180e0e3/593fc6f6N2d63d1a0.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）欧式油烟机家用抽油烟机 吸油烟机 悦界系列 大吸力免拆洗 CXW-200-67A1",
                        "CustomAttrList" : "欧式^排风量19(m3\x2Fmin)^大吸力",
                        "shortWarename" : "老板（Robam） 67A1油烟机"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "22954",
                    "dredisprice": "2499.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272637952",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "5238914",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/10331/36/11106/70985/5c6cc4abEe05884ef/8658a7dcb741e50b.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）大吸力 免拆洗欧式抽油烟机灶具套装60Q5+32B2（天然气）",
                        "CustomAttrList" : "欧式^排风量17(m3\x2Fmin)^静音",
                        "shortWarename" : "老板（Robam） 60Q5烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "35718",
                    "dredisprice": "2979.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435456",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "978182",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t27223/3/2029985771/136868/89e790b1/5bf4ebd6Na56d7b89.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）悦界系列 大吸力欧式触控抽油烟机燃气灶具套装67A1+56B0（天然气）",
                        "CustomAttrList" : "欧式^排风量19(m3\x2Fmin)^一级能效",
                        "shortWarename" : "老板（Robam） 67A1烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "78685",
                    "dredisprice": "3999.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435458",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4376443",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t6454/205/1621277076/82795/e75a221e/5954c7c8N142cfd18.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）侧吸式油烟机家用抽油烟机 吸油烟机 CXW-200-21A5",
                        "CustomAttrList" : "侧吸式^排风量17(m3\x2Fmin)^静音",
                        "shortWarename" : "老板（Robam） 21A5油烟机"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "19233",
                    "dredisprice": "2099.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272637952",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4444445",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t20728/152/1742613311/76121/2b522ee7/5b32ff83Nd4936e7e.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam） 侧吸式油烟机家用抽油烟机 吸油烟机 挥手爆炒 巨幕拢烟 CXW-200-27A3",
                        "CustomAttrList" : "侧吸式^排风量19(m3\x2Fmin)^一级能效",
                        "shortWarename" : "老板（Robam） 27A3油烟机"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "9741",
                    "dredisprice": "2999.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272637952",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4324018",
                    "property_flag": "0",
                    "flags": "4722816"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t2020/183/2774785948/36506/667be2d2/56e8c4c8Nf65a4683.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）大吸力免拆洗油烟机单机 欧式家用抽油烟机 CXW-200-60Q5",
                        "CustomAttrList" : "欧式^排风量17(m3\x2Fmin)^大吸力",
                        "shortWarename" : "老板（Robam） 60Q5油烟机"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "40200",
                    "dredisprice": "1999.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443648",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "1228509",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t20962/117/2096147311/167531/38b22840/5b46f226N79eddfeb.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板 （Robam）燃气灶 嵌入式煤气灶具 家用双灶具嵌可用天然气  猛火匀喷 4.2kW 不锈钢JZT-32G5（天然气）",
                        "CustomAttrList" : "天然气12T^不锈钢^1级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "6377",
                    "dredisprice": "1399.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272637952",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "8145210",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/18537/18/5263/193526/5c3bf6b2E2a42abaf/d3acf556198afeea.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板 （Robam）燃气灶 嵌入式煤气灶具 家用双灶具嵌可用天然气  猛火匀喷 4.2KW钢化玻璃JZT-32B2（天然气）",
                        "CustomAttrList" : "天然气12T^钢化玻璃^1级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "40966",
                    "dredisprice": "1399.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "1346379776",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "7325806",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/17176/31/5388/162158/5c3bf991E9b48009b/4dc1c471a4f10854.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）燃气灶 嵌入式煤气灶具 家用双灶具嵌可用 天然气 黑钻系列 4.5KW大火力 JZT-37B2（天然气）",
                        "CustomAttrList" : "天然气12T^钢化玻璃^1级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "10348",
                    "dredisprice": "2099.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "1346379776",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100000491361",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/37009/23/14074/180625/5d253772Ed50766be/7f9151f49a05ed75.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）悦界系列抽油烟机灶具套装 家用吸油烟机燃气灶排烟灶套装67A7+56B0（天然气）",
                        "CustomAttrList" : "塔形^排风量20(m3\x2Fmin)及以上^一级能效",
                        "shortWarename" : "老板（Robam） 67A7烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "14637",
                    "dredisprice": "5299.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435458",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "5394398",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t21919/255/2227627354/96908/d59466be/5b4d4de7N902da6f4.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）大吸力 免拆洗触控侧吸式抽油烟机 26A5S+32B2（天然气）",
                        "CustomAttrList" : "侧吸式^排风量19(m3\x2Fmin)^触控控制",
                        "shortWarename" : "老板（Robam） 26A5S烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "19289",
                    "dredisprice": "3799.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435458",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4903500",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/26722/23/13698/103709/5ca1d188E5ca0bec2/edf313ba4d6c2ead.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）欧式油烟机家用抽油烟机 吸油烟机 挥手智控欧式触屏 20立方大风量CXW-200-67A1H",
                        "CustomAttrList" : "欧式^排风量20(m3\x2Fmin)及以上^一级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "7137",
                    "dredisprice": "2899.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272654338",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100004558824",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/83107/17/4853/159979/5d2fc9c9E790867cf/f2098271bcd00646.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）万有吸力 侧吸式抽油烟机 燃气灶具套装 25A7+37B2（天然气）",
                        "CustomAttrList" : "侧吸式^排风量20(m3\x2Fmin)及以上^触控控制",
                        "shortWarename" : "老板（Robam） 25A7烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "15127",
                    "dredisprice": "4799.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435458",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "6280100",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/16177/28/12354/76498/5c984ee8E14451a8f/cd4ec5a62e03a2e7.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）大吸力 免拆洗触控欧式抽油烟机 CXW-200-63D1",
                        "CustomAttrList" : "欧式^排风量17(m3\x2Fmin)^触控控制",
                        "shortWarename" : "老板（Robam） 63D1油烟机"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "5683",
                    "dredisprice": "3899.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443648",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "6321132",
                    "property_flag": "0",
                    "flags": "4722816"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/26789/30/5204/193987/5c3bf947E3d025dd6/7e9ffc9dddcf8b48.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）燃气灶 嵌入式煤气灶具 家用双灶具嵌可用（液化气）JZY-33B7",
                        "CustomAttrList" : "液化气20Y^钢化玻璃^2级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "21737",
                    "dredisprice": "1199.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "272629760",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "3677714",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/27492/38/6031/105812/5c454e76E3314f1aa/0cb426c23cd6a897.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）侧吸式油烟机家用抽油烟机 吸油烟机 大吸力免拆洗 CXW-200-21A6",
                        "CustomAttrList" : "侧吸式^排风量17(m3\x2Fmin)^静音",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "1098",
                    "dredisprice": "2099.00",
                    "good": "95",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "28800",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100003047334",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/33576/37/6822/130072/5cbedb0cE8beee245/06a83fb4639509bc.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）抽油烟机灶具套装 家用吸油烟机燃气灶排烟灶套装 25X1+32B2（天然气）",
                        "CustomAttrList" : "侧吸式^排风量20(m3\x2Fmin)及以上^静音",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "4043",
                    "dredisprice": "4099.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268460034",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100003852274",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/5214/19/6547/251070/5ba32cfbE06c7d340/b14c8e3bbb637e4e.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）魔厨升级新品蒸箱嵌入式大容量40L智能触控外置水箱蒸汽炉ZQB400-S270A",
                        "CustomAttrList" : "",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13882",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "810",
                    "dredisprice": "5999.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443650",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100000540912",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/49326/24/2119/139322/5cff5692E3676a95f/35303dea710e092b.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）悦界系列 大吸力欧式触控  抽油烟机灶具套装67A3+32B2（天然气）",
                        "CustomAttrList" : "欧式^排风量19(m3\x2Fmin)^一级能效",
                        "shortWarename" : "老板（Robam） 67A3烟灶套装"
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "13755",
                    "dredisprice": "4099.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268435456",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "4376393",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/28792/14/2006/50535/5c18b828E9da6309e/1b3e759ee77b8a1a.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板(Robam)消毒柜 消毒嵌入式厨房碗柜家用 茶杯碗筷消毒100L大容量 晶钻内胆 ZTD100C-703",
                        "CustomAttrList" : "嵌入式^81-100L^臭氧消毒",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1301",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "5179",
                    "dredisprice": "2499.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443648",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "6084969",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/23584/25/4697/131215/5c35370bE58d09691/161c490bcf43cc58.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）蒸箱 嵌入式 40L全屏触控外置水箱蒸汽炉ZQB400-S273",
                        "CustomAttrList" : "",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13882",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "3827",
                    "dredisprice": "4299.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443650",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "6098732",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/3261/11/6666/123323/5ba371dbEd64a7078/b8487a31910d1b8c.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）魔厨烤箱嵌入式 40L大容量智能便捷触控家用嵌入式电烤箱 KQWS-2150-R070A",
                        "CustomAttrList" : "",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13882",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "321",
                    "dredisprice": "4999.00",
                    "good": "100",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "276832256",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100000540930",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/39805/21/2256/77950/5cc00abeE86e904b9/20da57f7fe7484c2.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam） 大吸力免拆洗触控侧吸式家用抽油烟机燃气灶套装  27A3H+57B2（天然气）",
                        "CustomAttrList" : "侧吸式^排风量20(m3\x2Fmin)及以上^一级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "814",
                    "dredisprice": "5899.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "28800",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100005268556",
                    "property_flag": "0",
                    "flags": "4722816"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t25915/259/993782040/128888/ee3f0f9c/5b84a76bN62cd959e.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）燃气灶 嵌入式灶具 家用灶具 猛火节能钢化玻璃（液化气）JZ(Y\x2FT\x2FR)-56B0",
                        "CustomAttrList" : "液化气20Y^钢化玻璃^1级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "23724",
                    "dredisprice": "1599.00",
                    "good": "99",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443648",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "5238944",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/36706/30/5609/140097/5cc012e3E357a6baa/f00507217f20ee0d.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）嵌入式燃气灶 猛火煤气灶5.0kW 天然气灶具JTZ-57B2",
                        "CustomAttrList" : "天然气12T^钢化玻璃^1级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "388",
                    "dredisprice": "2499.00",
                    "good": "95",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "1073770624",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100005228504",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/20548/5/12418/202868/5c998c84E11de9be6/b8b5bab71449c89d.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）燃气灶具天然气双灶不锈钢家用煤气灶JZT-36G3",
                        "CustomAttrList" : "天然气12T^不锈钢^1级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "13298",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "450",
                    "dredisprice": "1599.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "28800",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100004404216",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/38323/14/2308/83537/5cc00b30Ec2bd7a4b/6c4732dde3851a40.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）抽油烟机灶具 家用吸油烟机燃气灶 烟灶套装 25A7+57B2（天然气）",
                        "CustomAttrList" : "侧吸式^排风量20(m3\x2Fmin)及以上^一级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "154",
                    "dredisprice": "4999.00",
                    "good": "100",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "28802",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100004883498",
                    "property_flag": "0",
                    "flags": "21500032"
                },

                {
                    "Content": {
                        "author": "",
                        "imageurl": "jfs/t1/67977/6/5284/144335/5d366317E78d426cf/481cd9b08efe35af.jpg",
                        "long_image_url": "",
                        "shop_name": "",
                        "warename": "老板（Robam）侧吸式油烟机灶具 家用吸油烟机燃气灶排烟灶套装 27A7+37B2（天然气）",
                        "CustomAttrList" : "侧吸式^排风量20(m3\x2Fmin)及以上^一级能效",
                        "shortWarename" : ""
                    },


                    "pinGou": {
                        "bp": "",
                        "count": ""
                    },
                    "catid": "1300",
                    "cid1": "737",
                    "cid2": "13297",
                    "commentcount": "1760",
                    "dredisprice": "7099.00",
                    "good": "98",
                    "hotscore": "8.",
                    "hprice": "",
                    "ico": "0",
                    "productext": "268443650",
                    "shop_id": "1000001402",
                    "vender_id": "1000001402",
                    "wareid": "100001238814",
                    "property_flag": "0",
                    "flags": "21500032"
                }

            ]
        }
    }
}
wareidList = []
print(type(data))
data = json.dumps(data)

data = json.loads(data)

print(type(data))
wareid = jsonpath.jsonpath(data,"$..wareid")
wareidList.append(wareid)


for temp  in wareidList[0]:
    dpUrl = "https://cd.jd.com/promotion/v2?callback=jQuery7173151&skuId={}&area=13_1000_40489_40616&shopId=1000001402&cat=737%2C13297%2C13882".format(str(temp))

    dpData = request.urlopen(dpUrl).read().decode("gbk")


    char_i = "("
    charIndex = dpData.index(char_i)

    dpData = dpData[charIndex+1:-1]

    dpData = str(dpData)



    dpData = json.loads(dpData)
    print(type(dpData))


    ads = jsonpath.jsonpath(dpData,"$..adsStatus")
    print(ads)









