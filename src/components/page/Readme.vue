<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-setting"></i> 简介</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="ms-doc">
            <h3>README.md</h3>
            <article>
<!--                 <h1>manage-system</h1>
                <p>基于Vue.js 2.x系列 + Element UI 的后台管理系统解决方案</p> -->
                <h2>前言</h2>
                <img width="150" height="150" src="../../assets/head.png" style="float: left;margin-right: 30px"><p style="height: 150px;line-height:30px; text-indent: 30px; padding-top: 20px;">近年来，脑部疾病以其高发病率、高死亡率、高致残率、高复发率以及多并发症等特点成为威胁人类健康的重要因素。磁共振成像（MRI）技术由于非介入、无损伤以及运动不受目标运动影响等特点，成为临床诊断的重要辅助手段。本系统作为对脑磁共振图像的可视化和管理平台，为医生和研究人员提供便利，实现数据的共享。</p>
                <h2>特点</h2>
                <el-checkbox disabled checked>领先的 web 技术</el-checkbox>
                <br>
                <el-checkbox disabled checked>实时高效、跨平台</el-checkbox>
                <br>
                <el-checkbox disabled checked>直接操作 DICOM 图像</el-checkbox>
                <br>
                <el-checkbox disabled checked>图像分割</el-checkbox>
                <br>
            </article>
        </div>

    </div>
</template>

<script>
    export default {
        data: function(){
            return {}
        }
    }
</script>

<style scoped>
    .ms-doc{
        width:100%;
        max-width: 980px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }
    .ms-doc h3{
        padding: 9px 10px 10px;
        margin: 0;
        font-size: 14px;
        line-height: 17px;
        background-color: #f5f5f5;
        border: 1px solid #d8d8d8;
        border-bottom: 0;
        border-radius: 3px 3px 0 0;
    }
    .ms-doc article{
        padding: 45px;
        word-wrap: break-word;
        background-color: #fff;
        border: 1px solid #ddd;
        border-bottom-right-radius: 3px;
        border-bottom-left-radius: 3px;
    }
    .ms-doc article h1{
        font-size:32px;
        padding-bottom: 10px;
        margin-bottom: 15px;
        border-bottom: 1px solid #ddd;
    }
    .ms-doc article h2 {
        margin: 24px 0 16px;
        font-weight: 600;
        line-height: 1.25;
        padding-bottom: 7px;
        font-size: 24px;
        border-bottom: 1px solid #eee;
    }
    .ms-doc article p{
        margin-bottom: 15px;
        line-height: 1.5;
    }
    .ms-doc article .el-checkbox{
        margin-bottom: 5px;
    }
</style>