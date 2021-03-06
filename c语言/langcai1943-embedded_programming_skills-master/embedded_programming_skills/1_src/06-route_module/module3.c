/*******************************************************************************
 * Copyleft (c) 2020 将狼才鲸
 *
 * \file    module3.c
 * \brief   用于路由单元测试的模块1
 * \author  将狼才鲸
 * \version 1.0.0
 * \date    2020-05-17
 * \license MulanPSL-1.0
 *
 * -----------------------------------------------------------------------------
 *
 * -----------------------------------------------------------------------------
 * 文件修改历史：
 * <时间>       | <版本>    | <作者>    | <描述>
 * 2020-05-17   | v1.0.0    | 将狼才鲸  | 创建文件
 * -----------------------------------------------------------------------------
 ******************************************************************************/

/*================================= 头 文 件 =================================*/
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include "module3.h"
#include "route.h"

/*================================= 全局变量 =================================*/
static ROUTE_ITEM my_route;

/*================================= 私有函数 =================================*/
/*!
 * \brief 模块3接收从路由来的数据
 *
 * \param[in] src 源模块ID，从那个模块发过来的，可根据此模块的特性解析数据
 * \param[in] dst 目的模块ID，即本模块ID
 * \param[in] buf 输入的数据
 * \param[in] len 输入的数据长度
 * \return    0处理正常，负数错误码
 */
static int module3_recv(int src, int dst, char *buf, int len)
{
    //TODO: 参数检查

    if (dst != MODULE3_ID)
        pr_err("%s error! dst id: %d, my id: %d",
               __func__, dst, MODULE3_ID);

    pr_info("【模块3】收到数据：%.*s\n", len, buf);

    return 0;
}

/*================================= 接口函数 =================================*/
/*!
 * \brief 注册本模块的路由接口
 *
 * 如果本模块是一个通讯模块，那么可以注册两个接口，一个将数据从通讯口发送出去的，
 * 一个是本模块要使用的，如配置信息，控制信息等
 * \return    0处理正常，负数错误码
 */
int module3_init(void)
{
    my_route.src = MODULE3_ID;
    my_route.dst = MODULE1_ID;
    my_route.recv = route_recv;
    my_route.send = module3_recv;
    route_register(&my_route);

    return 0;
}

/*!
 * \brief 模块轮询接口
 *
 * 可以在这个函数里持续监测通讯链路上输入的数据，有数据则进行处理
 *
 * \return 0处理正常，负数错误码
 */
int module3_run(void)
{
    //TODO:从链路中获取数据

#ifdef MODULE3_UNITEST
#define _3STR1 "这是【模块3】发送给模块1的数据"
#define _3STR2 "这是【模块3】发送给模块2的数据"
#define _3STR3 "这是【模块3】发送给模块3的数据"
    my_route.recv(MODULE3_ID, MODULE1_ID, _3STR1, strlen(_3STR1) + 1);
    my_route.recv(MODULE3_ID, MODULE2_ID, _3STR2, strlen(_3STR2) + 1);
    my_route.recv(MODULE3_ID, MODULE3_ID, _3STR3, strlen(_3STR1) + 1);
    pr_info("==================");
    sleep(2);
#endif /* MODULE3_UNITEST */

    return 0;
}

/*!
 * \brief 模块注销
 *
 * \return 0处理正常，负数错误码
 */
int module3_exit(void)
{

    return 0;
}
