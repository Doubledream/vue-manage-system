<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 查询</el-breadcrumb-item>
                <el-breadcrumb-item>个人详情</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="left-content">
            <el-button type="text" @click="back">跳转至查询页面<i class="el-icon-share"></i></el-button>
            <br>
            <div id="dwv">
                <div class="layerContainer">
                    <canvas class="imageLayer"></canvas>
                </div>
            </div>
            <input type="range" id="sliceRange" value="0">
            <ul id="patientTags"></ul>
        </div>
        <div id="imageTags">
            <el-table :data="tableData" border style="width:auto;font-size:10px" ref="multipleTable" height="500">
                <el-table-column prop="name" label="名称"  width="200">
                </el-table-column>
                <el-table-column prop="value" label="值" :formatter="formatter">
                </el-table-column>
                <el-table-column prop="group" label="组" width="80">
                </el-table-column>
                <el-table-column prop="element" label="元素" width="80">
                </el-table-column>
                <el-table-column prop="vl" label="VL" width="55">
                </el-table-column>
                <el-table-column prop="vr" label="VR" width="55">
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                tableData: [],
                patient: {
                    name: "董文琴",
                    age: 50,
                    gender: "女",
                    registerDate: "2016-10-08",
                    tel: "13851580146",
                    address: "南京市玄武区",
                    source: "南京市第一医院",
                    remarks: null,
                },
                dcmAnalyze: {
                    'x00020000': 'FileMetaInformationGroupLength',
                    'x00020001': 'FileMetaInformationVersion',
                    'x00020002': 'MediaStorageSOPClassUID',
                    'x00020003': 'MediaStorageSOPInstanceUID',
                    'x00020010': 'TransferSyntaxUID',
                    'x00020012': 'ImplementationClassUID',
                    'x00020013': 'ImplementationVersionName',
                    'x00080005': 'SpecificCharacterSet',
                    'x00080008': 'ImageType',
                    'x00080012': 'InstanceCreationDate',
                    'x00080013': 'InstanceCreationTime',
                    'x00080014': 'InstanceCreatorUID',
                    'x00080016': 'SOPClassUID',
                    'x00080018': 'SOPInstanceUID',
                    'x00080020': 'StudyDate',
                    'x00080021': 'SeriesDate',
                    'x00080022': 'AcquisitionDate',
                    'x00080023': 'ContentDate',
                    'x00080030': 'StudyTime',
                    'x00080031': 'SeriesTime',
                    'x00080032': 'AcquisitionTime',
                    'x00080033': 'ContentTime',
                    'x00080050': 'AccessionNumber',
                    'x00080060': 'Modality',
                    'x00080070': 'Manufacturer',
                    'x00080080': 'InstitutionName',
                    'x00080090': 'ReferringPhysicianName',
                    'x00081010': 'StationName',
                    'x00081030': 'StudyDescription',
                    'x0008103E': 'SeriesDescription',
                    'x00081040': 'InstitutionalDepartmentName',
                    'x00081070': 'OperatorsName',
                    'x00081080': 'AdmittingDiagnosesDescription',
                    'x00081090': 'ManufacturerModelName',
                    'x00081111': 'ReferencedPerformedProcedureStepSequence',
                    'x00081140': 'ReferencedImageSequence',
                    'x00100010': 'PatientName',
                    'x00100020': 'PatientID',
                    'x00100030': 'PatientBirthDate',
                    'x00100040': 'PatientSex',
                    'x00101000': 'OtherPatientIDs',
                    'x00101030': 'PatientWeight',
                    'x001021C0': 'PregnancyStatus'
                }
            }
        },
        methods: {
            back() {
                this.$router.push({path: '/basetable'});
            },
            formatter(row, column) {
                return row.value;
            },
            drawImage() {
                // base function to get elements
                dwv.gui.getElement = dwv.gui.base.getElement;
                dwv.gui.displayProgress = function (percent) {};

                // create the dwv app
                var app = new dwv.App();
                // initialise with the id of the container div
                app.init({
                    "containerDivId": "dwv",
                    "tools": ["Scroll"]
                });
                // load dicom data
                app.loadURLs(["https://raw.githubusercontent.com/ivmartel/dwv/master/tests/data/bbmri-53323851.dcm","https://raw.githubusercontent.com/ivmartel/dwv/master/tests/data/bbmri-53323707.dcm","https://raw.githubusercontent.com/ivmartel/dwv/master/tests/data/bbmri-53323563.dcm"]);

                var range = document.getElementById("sliceRange");
                range.min = 0;
                app.addEventListener("load-end", function () {
                    range.max = app.getImage().getGeometry().getSize().getNumberOfSlices() - 1;
                });
                app.addEventListener("slice-change", function () {
                    range.value = app.getViewController().getCurrentPosition().k;
                });
                range.oninput = function () {
                    var pos = app.getViewController().getCurrentPosition();
                    pos.k = this.value;
                    app.getViewController().setCurrentPosition(pos);
                }
            },
            tags() {
                var url = "static/img/IM_0014.dcm";
                var self = this;

                var onload = function () {
                    // setup the dicom parser
                    var dicomParser = new dwv.dicom.DicomParser();
                    // parse the buffer
                    dicomParser.parse(this.response);
                    // div to display text
                    var div = document.getElementById("imageTags");
                    var rawTags = dicomParser.getRawDicomElements();
                    // div.appendChild(document.createTextNode(
                    //     "Modality: " + rawTags.x00080060.value[0]
                    // ));
                    // get the wrapped dicom tags
                    console.log(rawTags);
                    var arr = [];
                    for (let i in self.dcmAnalyze) {
                        var json = {};
                        json.name = self.dcmAnalyze[i];
                        json.value = rawTags[i].value[0];
                        json.group = rawTags[i].tag.group;
                        json.element = rawTags[i].tag.element;
                        json.vl = rawTags[i].vl;
                        json.vr = rawTags[i].vr;
                        arr.push(json);
                    }
                    self.tableData = arr;
                };

                var request = new XMLHttpRequest();
                request.open('GET', url, true);
                request.responseType = "arraybuffer";
                request.onload = onload;
                request.send(null);
            },
            info() {
                var translate = {
                    name: '姓名',
                    age: '年龄',
                    gender: '性别',
                    registerDate: '登记日期',
                    tel: '电话号码',
                    address: '家庭住址',
                    source: '就诊来源',
                    remarks: '备注'
                };
                var ul = document.getElementById("patientTags");
                var html = '';
                for (let i in this.patient) {
                    html += '<li><span>' + translate[i] + ': </span><span>' + this.patient[i] +'</span></li>'
                }
                ul.innerHTML = html;
            }
        },
        computed: {
        },
        mounted() {
            this.drawImage();
            this.info();
            this.tags();
        }
    }
</script>

<style>
    .left-content {
        width: 300px;
        float: left;
    }
    #patientTags {
        font-size: 14px;
        line-height: 20px;
        padding: 5px;
        color: #333;
        width: 259px;
    }
    #patientTags li{
        list-style-type: none;
    }
</style>