<template>
<div class="dicomWebViewer">
    <div id="dwv">
        <div id="pageHeader">
            <!-- <h1>DWV <span class="dwv-version"></span></h1> -->
            <div class="toolbar"></div>
        </div>
        <div id="pageMain">
            <div class="openData" title="File">
                <div class="loaderlist"></div>
                <div id="progressbar"></div>
            </div>

            <div class="toolList" title="Toolbox"></div>
            <div class="history" title="History"></div>
            <div class="tags" title="Tags"></div>
            <div class="drawList" title="Draw list"></div>
            <div class="help" title="Help"></div>

            <div class="layerDialog" title="Image">
                <div class="dropBox"></div>
                <div class="layerContainer">
                    <canvas class="imageLayer">Only for HTML5 compatible browsers...</canvas>
                    <div class="drawDiv"></div>
                    <div class="infoLayer">
                        <div class="infotl"></div>
                        <div class="infotc"></div>
                        <div class="infotr"></div>
                        <div class="infocl"></div>
                        <div class="infocr"></div>
                        <div class="infobl"></div>
                        <div class="infobc"></div>
                        <div class="infobr" style="bottom: 64px;"></div>
                        <div class="plot"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
    // import dwv from 'dwv';
    export default {
        data() {
            return {
            }
        },
        methods: {
        }
    }
</script>

<style>
    .dicomWebViewer {
        background-color: #222;
        color: white;
        font-size: 80%;
    }
/*    #pageHeader h1 {
        display: inline-block;
        margin: 0;
        color: #fff;
    }
    #pageHeader a {
        color: #ddf;
    }*/
    #pageHeader .toolbar {
/*        display: inline-block;
        float: right;*/
        position: absolute;
        top: 5px;
        right: 0;
/*        margin-top: -30px;*/
    }
    .toolList ul {
        padding: 0;
    }
    .toolList li {
        list-style-type: none;
    }
    #pageMain {
        position: absolute;
        height: 92%;
        width: 99%;
        bottom: 5px;
        left: 5px;
        background-color: #333;
    }
    .infotl {
        text-shadow: 0 1px 0 #000;
    }
    .infotc {
        text-shadow: 0 1px 0 #000;
    }
    .infotr {
        text-shadow: 0 1px 0 #000;
    }
    .infocl {
        text-shadow: 0 1px 0 #000;
    }
    .infocr {
        text-shadow: 0 1px 0 #000;
    }
    .infobl {
        text-shadow: 0 1px 0 #000;
    }
    .infobc {
        text-shadow: 0 1px 0 #000;
    }
    .infobr {
        text-shadow: 0 1px 0 #000;
    }
    .dropBox {
        margin: 20px;
    }
    .ui-icon {
        zoom: 125%;
    }
    .tagsTable tr:nth-child(even) {
        background-color: #333;
    }
    .drawList tr:nth-child(even) {
        background-color: #333;
    }
    button, input, li, table {
        margin-top: 0.2em;
    }
    li button, li input {
        margin: 0;
    }
    .history_list {
        width: 100%;
    }
    .ui-widget-content {
        background-color: #222;
        background-image: url();
    }
</style>