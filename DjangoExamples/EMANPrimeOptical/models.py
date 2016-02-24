# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AckTable(models.Model):
    ackindex = models.IntegerField(primary_key=True)
    ackusername = models.CharField(max_length=64, blank=True, null=True)
    acktimestamp = models.DateField(blank=True, null=True)
    isautoack = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ack_table'


class ActiveAlarmTable(models.Model):
    nedbaccessid = models.IntegerField()
    alarmseqnum = models.BigIntegerField()
    moduleorifindex = models.BigIntegerField()
    activealarmtimestamp = models.DateField()
    activealarmtype = models.IntegerField()
    activealarmseverity = models.BooleanField()
    activealarmserveff = models.BooleanField()
    activealarmadditionalinfo = models.CharField(max_length=512, blank=True, null=True)
    ackindex = models.IntegerField()
    activealarmflag = models.NullBooleanField()
    activealarmcomment = models.CharField(max_length=2014, blank=True, null=True)
    clearalarmtimestamp = models.DateField(blank=True, null=True)
    nealarmtimestamp = models.DateField()
    activealarmindex = models.BigIntegerField()
    moduletype = models.IntegerField(blank=True, null=True)
    physicalloc = models.BigIntegerField()
    alarmstatus = models.BooleanField()
    nealarmcleartimestamp = models.DateField(blank=True, null=True)
    externalcondition = models.CharField(max_length=1024, blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField()
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    direction = models.CharField(max_length=8, blank=True, null=True)
    location = models.CharField(max_length=4, blank=True, null=True)
    modelname = models.CharField(max_length=1024, blank=True, null=True)
    affectedobject = models.CharField(max_length=1024, blank=True, null=True)
    modellocation = models.CharField(max_length=1024, blank=True, null=True)
    layerrate = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_alarm_table'
        unique_together = (('nedbaccessid', 'moduleorifindex', 'activealarmtype', 'nealarmtimestamp', 'physicalloc', 'objecttype', 'alarmseqnum'),)


class AdditionalDeviceInfo(models.Model):
    deviceid = models.IntegerField(primary_key=True)
    nedbaccessid = models.IntegerField()
    phyloc = models.BigIntegerField()
    moduletype = models.IntegerField()
    state = models.BooleanField()
    isconnected = models.BooleanField()
    discoverystate = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'additional_device_info'


class AdjacencyTable(models.Model):
    layer = models.IntegerField()
    tpmodelname = models.CharField(max_length=765)
    nedbaccessid = models.IntegerField()
    peertp = models.CharField(max_length=765)
    peeripaddress = models.BigIntegerField()
    adjcost = models.IntegerField(blank=True, null=True)
    adjprot = models.IntegerField(blank=True, null=True)
    adjsize = models.IntegerField(blank=True, null=True)
    adjstate = models.IntegerField(blank=True, null=True)
    localipaddress = models.BigIntegerField(blank=True, null=True)
    localtp = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adjacency_table'
        unique_together = (('layer', 'tpmodelname', 'nedbaccessid', 'peertp', 'peeripaddress'),)


class AdminJobTable(models.Model):
    jobid = models.BigIntegerField()
    taskid = models.BigIntegerField()
    jobtype = models.IntegerField()
    jobowner = models.CharField(max_length=64, blank=True, null=True)
    nedbaccessid = models.ForeignKey('NeInfoTable', db_column='nedbaccessid', blank=True, null=True)
    jobstatus = models.NullBooleanField()
    creationtime = models.DateField(blank=True, null=True)
    scheduledtime = models.DateField(blank=True, null=True)
    starttime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    additionalinfo = models.CharField(max_length=4000, blank=True, null=True)
    usercomments = models.CharField(max_length=2048, blank=True, null=True)
    operation_info = models.CharField(max_length=4000, blank=True, null=True)
    display_info = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_job_table'
        unique_together = (('jobid', 'taskid'),)


class AlarmAckConfigTable(models.Model):
    configalarmack = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'alarm_ack_config_table'


class AlarmCountTable(models.Model):
    nedbaccessid = models.IntegerField()
    ackalarmcount = models.BigIntegerField(blank=True, null=True)
    clearedalarmcount = models.BigIntegerField(blank=True, null=True)
    criticalalarmcount = models.BigIntegerField(blank=True, null=True)
    majoralarmcount = models.BigIntegerField(blank=True, null=True)
    minoralarmcount = models.BigIntegerField(blank=True, null=True)
    warningalarmcount = models.BigIntegerField(blank=True, null=True)
    usertypeid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'alarm_count_table'
        unique_together = (('nedbaccessid', 'usertypeid'),)


class AlarmEventCauseTable(models.Model):
    enumindex = models.IntegerField(primary_key=True)
    enumstring = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alarm_event_cause_table'


class AlarmEventTable(models.Model):
    nedbaccessid = models.IntegerField()
    eventindex = models.IntegerField()
    moduleorifindex = models.BigIntegerField()
    alarmeventtype = models.IntegerField()
    alarmeventtimestamp = models.DateField()
    alarmeventcause = models.IntegerField()
    alarmeventseverity = models.BooleanField()
    serviceeffecting = models.BooleanField()
    otherinfo = models.CharField(max_length=512, blank=True, null=True)
    moduletype = models.IntegerField(blank=True, null=True)
    physicalloc = models.BigIntegerField(blank=True, null=True)
    neeventtimestamp = models.DateField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    direction = models.CharField(max_length=8, blank=True, null=True)
    location = models.CharField(max_length=4, blank=True, null=True)
    modelname = models.CharField(max_length=1024, blank=True, null=True)
    affectedobject = models.CharField(max_length=1024, blank=True, null=True)
    modellocation = models.CharField(max_length=1024, blank=True, null=True)
    layerrate = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alarm_event_table'


class AlarmEventTypeEnumTable(models.Model):
    enumindex = models.IntegerField(primary_key=True)
    enumstring = models.CharField(max_length=128, blank=True, null=True)
    tl1string = models.CharField(max_length=64, blank=True, null=True)
    tmfstring = models.CharField(max_length=64, blank=True, null=True)
    eventtype = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'alarm_event_type_enum_table'


class AlarmFilteredProfileTable(models.Model):
    probablecauseid = models.ForeignKey(AlarmEventTypeEnumTable, db_column='probablecauseid')
    usertypeid = models.ForeignKey('UserTypeTable', db_column='usertypeid')

    class Meta:
        managed = False
        db_table = 'alarm_filtered_profile_table'
        unique_together = (('probablecauseid', 'usertypeid'),)


class ApcDomainTable(models.Model):
    nedbaccessid = models.IntegerField()
    sideout = models.IntegerField()
    apcstate = models.IntegerField(blank=True, null=True)
    apcadminstate = models.IntegerField(blank=True, null=True)
    sides = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apc_domain_table'
        unique_together = (('nedbaccessid', 'sideout'),)


class ApsGroupTable(models.Model):
    nedbaccessid = models.ForeignKey('NeInfoTable', db_column='nedbaccessid')
    groupname = models.CharField(max_length=64)
    configmode = models.IntegerField(blank=True, null=True)
    configrevert = models.IntegerField(blank=True, null=True)
    configdirection = models.IntegerField(blank=True, null=True)
    configcreationtime = models.DateField(blank=True, null=True)
    configspan = models.IntegerField(blank=True, null=True)
    protectiontype = models.IntegerField(blank=True, null=True)
    ycableconfig = models.IntegerField(blank=True, null=True)
    switchedchannelstatus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aps_group_table'
        unique_together = (('nedbaccessid', 'groupname'),)


class AuditLogMappingTable(models.Model):
    usertype = models.IntegerField(blank=True, null=True)
    actualname = models.CharField(max_length=256, blank=True, null=True)
    currentname = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log_mapping_table'


class AuditLogTable(models.Model):
    timestamp = models.DateField(blank=True, null=True)
    module = models.IntegerField()
    filename = models.CharField(max_length=256, blank=True, null=True)
    linenumber = models.IntegerField(blank=True, null=True)
    logmessage = models.CharField(max_length=1024, blank=True, null=True)
    nedbaccessid = models.IntegerField()
    service = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'audit_log_table'


class BlsrNode(models.Model):
    blsrid = models.IntegerField()
    ringid = models.CharField(max_length=8)
    nodeid = models.IntegerField()
    ringnodeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blsr_node'


class BlsrSpan(models.Model):
    blsrid = models.IntegerField()
    ringid = models.CharField(max_length=8)
    linkid = models.IntegerField()
    workingspan = models.BooleanField()
    westnodeid = models.IntegerField()
    eastnodeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blsr_span'


class BlsrTable(models.Model):
    blsrid = models.IntegerField()
    ringid = models.CharField(max_length=8)
    ringtype = models.IntegerField()
    linerate = models.IntegerField()
    status = models.CharField(max_length=12)
    ringreversion = models.DecimalField(max_digits=8, decimal_places=2)
    spanreversion = models.DecimalField(max_digits=8, decimal_places=2)
    nodes = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'blsr_table'


class BridgeGroupTable(models.Model):
    toponodeid = models.ForeignKey('L2VlanTable', db_column='toponodeid')
    topouniqueid = models.ForeignKey('L2VlanTable', db_column='topouniqueid')
    vlan_number = models.ForeignKey('L2VlanTable', db_column='vlan_number')
    neid = models.IntegerField()
    slot_number = models.IntegerField()
    bridge_group_number = models.IntegerField()
    bridge_protocol = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridge_group_table'
        unique_together = (('neid', 'slot_number', 'bridge_group_number'),)


class CMetadata(models.Model):
    tableid = models.IntegerField(primary_key=True)
    tablename = models.CharField(max_length=30)
    tablejdaqname = models.CharField(max_length=128, blank=True, null=True)
    tabletype = models.NullBooleanField()
    title = models.CharField(max_length=132, blank=True, null=True)
    report = models.CharField(max_length=132, blank=True, null=True)
    reportfile = models.CharField(max_length=132, blank=True, null=True)
    titleiconstr = models.CharField(max_length=132, blank=True, null=True)
    help = models.CharField(max_length=132, blank=True, null=True)
    helpstrfilterdlg = models.CharField(max_length=132, blank=True, null=True)
    dbcolcount = models.IntegerField(blank=True, null=True)
    tcacolindex = models.IntegerField(blank=True, null=True)
    defsortcol = models.IntegerField(blank=True, null=True)
    filtermask = models.IntegerField(blank=True, null=True)
    autoref = models.NullBooleanField()
    disprowcount = models.IntegerField(blank=True, null=True)
    coldisprow = models.IntegerField(blank=True, null=True)
    colcount = models.IntegerField(blank=True, null=True)
    btnmask = models.BigIntegerField(blank=True, null=True)
    nedbaccessidcolindb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_metadata'


class CMetadataAttrPresentation(models.Model):
    metadataindex = models.IntegerField()
    attrindex = models.IntegerField()
    widget_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_metadata_attr_presentation'
        unique_together = (('metadataindex', 'attrindex'),)


class CMetadataCol(models.Model):
    tableid = models.ForeignKey(CMetadata, db_column='tableid')
    colname = models.CharField(max_length=50, blank=True, null=True)
    colheadertip = models.CharField(max_length=350, blank=True, null=True)
    colwidth = models.IntegerField(blank=True, null=True)
    displayorder = models.IntegerField(blank=True, null=True)
    sortable = models.NullBooleanField()
    editable = models.NullBooleanField()
    dbcolindex = models.IntegerField(blank=True, null=True)
    classname = models.CharField(max_length=128, blank=True, null=True)
    filtercol = models.IntegerField(blank=True, null=True)
    sortcolindb = models.IntegerField(blank=True, null=True)
    renderer = models.CharField(max_length=128, blank=True, null=True)
    colenumbases = models.IntegerField(blank=True, null=True)
    coltcabitindex = models.IntegerField(blank=True, null=True)
    colsortorder = models.NullBooleanField()
    isphysicalloccol = models.NullBooleanField()
    isinterfacecol = models.NullBooleanField()
    istimestampcol = models.NullBooleanField()
    identifier = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_metadata_col'


class CMetadataColCustom(models.Model):
    viewid = models.ForeignKey('CustomViewTable', db_column='viewid')
    colname = models.CharField(max_length=50)
    colwidth = models.IntegerField()
    displayorder = models.IntegerField()
    ishidden = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'c_metadata_col_custom'
        unique_together = (('viewid', 'colname'),)


class CMetadataFilter(models.Model):
    tableid = models.ForeignKey(CMetadata, db_column='tableid')
    filtercols = models.IntegerField(blank=True, null=True)
    initialfiltercols = models.IntegerField(blank=True, null=True)
    displayorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_metadata_filter'


class CMetadataGrpPresentation(models.Model):
    metadataindex = models.IntegerField()
    groupindex = models.IntegerField()
    parentindex = models.IntegerField()
    name = models.CharField(max_length=32, blank=True, null=True)
    displaytext = models.CharField(max_length=256, blank=True, null=True)
    attrclass = models.IntegerField(blank=True, null=True)
    attrtype = models.IntegerField(blank=True, null=True)
    enumval = models.CharField(max_length=1024, blank=True, null=True)
    attrgroup = models.IntegerField(blank=True, null=True)
    events = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_metadata_grp_presentation'
        unique_together = (('metadataindex', 'groupindex'),)


class CMetadataNetypes(models.Model):
    tableid = models.ForeignKey(CMetadata, db_column='tableid')
    netypes = models.CharField(max_length=15, blank=True, null=True)
    displayorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_metadata_netypes'


class CPropertySheetInfoTable(models.Model):
    modelindex = models.IntegerField(blank=True, null=True)
    propsheetindex = models.IntegerField(blank=True, null=True)
    tabindex = models.ForeignKey('CTabMetadataTable', db_column='tabindex', blank=True, null=True)
    tabposition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_property_sheet_info_table'


class CTabMetadataInfoTable(models.Model):
    tabindex = models.ForeignKey('CTabMetadataTable', db_column='tabindex', blank=True, null=True)
    subtabindex = models.IntegerField(blank=True, null=True)
    subtabposition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_tab_metadata_info_table'


class CTabMetadataTable(models.Model):
    tabindex = models.IntegerField(primary_key=True)
    tabname = models.CharField(max_length=200, blank=True, null=True)
    tabdataobjects = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    operationid = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_tab_metadata_table'


class CcatsizeTable(models.Model):
    sizename = models.CharField(max_length=64)
    ctmsize = models.IntegerField()
    ccatnum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ccatsize_table'


class CerentNeGroupTable(models.Model):
    nedbaccessid = models.ForeignKey('NeInfoTable', db_column='nedbaccessid')
    groupoption = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cerent_ne_group_table'


class ChangedTablesPatchesTable(models.Model):
    table_name_to_change = models.CharField(max_length=80, blank=True, null=True)
    columns_name_to_add = models.CharField(max_length=80, blank=True, null=True)
    sql_add_column = models.CharField(max_length=200, blank=True, null=True)
    sql_add_default = models.CharField(max_length=200, blank=True, null=True)
    force_creation = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changed_tables_patches_table'


class CircuitBsTbl(models.Model):
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    cktname = models.CharField(max_length=100, blank=True, null=True)
    cktdescription = models.CharField(max_length=256, blank=True, null=True)
    customerid = models.CharField(max_length=256, blank=True, null=True)
    serviceid = models.CharField(max_length=256, blank=True, null=True)
    ckttype = models.IntegerField(blank=True, null=True)
    cktsize = models.IntegerField(blank=True, null=True)
    cktdirection = models.NullBooleanField()
    cktismonitor = models.NullBooleanField()
    cktstate = models.IntegerField(blank=True, null=True)
    cktenhancedstate = models.IntegerField(blank=True, null=True)
    cktprotectiontype = models.IntegerField(blank=True, null=True)
    cktadditionalinfo = models.CharField(max_length=64, blank=True, null=True)
    cktcomment = models.CharField(max_length=2014, blank=True, null=True)
    cktuselap = models.NullBooleanField()
    cktochncchannel = models.IntegerField(blank=True, null=True)
    cktochncdir = models.NullBooleanField()
    isduplicatename = models.NullBooleanField()
    npid = models.IntegerField(blank=True, null=True)
    cktaliasname = models.CharField(max_length=100, blank=True, null=True)
    isopenvcat = models.NullBooleanField()
    isoverlay = models.NullBooleanField()
    isforportgrouping = models.NullBooleanField()
    isgmpls = models.NullBooleanField()
    lastchange = models.DateField(blank=True, null=True)
    terminology = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_bs_tbl'
        unique_together = (('cktnodeid', 'cktuniqueid'),)


class CircuitCtpTbl(models.Model):
    ctpaccessid = models.BigIntegerField()
    ctp_type = models.IntegerField()
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    cktctpnodeid = models.IntegerField(blank=True, null=True)
    cktctpnedbaccessid = models.IntegerField()
    cktctpmoduletype = models.IntegerField(blank=True, null=True)
    cktctpifindex = models.BigIntegerField(blank=True, null=True)
    cktctpobjecttype = models.IntegerField(blank=True, null=True)
    cktctpphysicalloc = models.BigIntegerField(blank=True, null=True)
    cktctpmodeltype = models.IntegerField(blank=True, null=True)
    cktctpdropprot = models.NullBooleanField()
    cktctppathprot = models.NullBooleanField()
    cktctpdropprottype = models.NullBooleanField()
    cktctpportname = models.CharField(max_length=64, blank=True, null=True)
    cktctpadditionalinfo = models.CharField(max_length=64, blank=True, null=True)
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)
    eqptinfoobjindex = models.IntegerField(blank=True, null=True)
    payloadtype = models.IntegerField(blank=True, null=True)
    modelkey = models.CharField(max_length=1024, blank=True, null=True)
    location = models.CharField(max_length=1024, blank=True, null=True)
    layerhierarchy = models.CharField(max_length=1024, blank=True, null=True)
    cktctpoldphysicalloc = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_ctp_tbl'


class CircuitDestTbl(models.Model):
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    cktdestnodeid = models.IntegerField(blank=True, null=True)
    cktdestmoduletype = models.IntegerField(blank=True, null=True)
    cktdestifindex = models.BigIntegerField(blank=True, null=True)
    cktdestobjecttype = models.IntegerField(blank=True, null=True)
    cktdestphysicalloc = models.BigIntegerField(blank=True, null=True)
    cktdestmodeltype = models.IntegerField(blank=True, null=True)
    cktdestdropprot = models.NullBooleanField()
    cktdestpathprot = models.NullBooleanField()
    cktdestdropprottype = models.NullBooleanField()
    cktdestportname = models.CharField(max_length=64, blank=True, null=True)
    cktdestadditionalinfo = models.CharField(max_length=64, blank=True, null=True)
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_dest_tbl'


class CircuitNodeBsTbl(models.Model):
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    nodeid = models.IntegerField()
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_node_bs_tbl'


class CircuitSizeTable(models.Model):
    userid = models.ForeignKey('UserTable', db_column='userid', blank=True, null=True)
    circuitsizetype = models.IntegerField(blank=True, null=True)
    circuitsizeid = models.IntegerField(blank=True, null=True)
    circuitsizename = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_size_table'


class CircuitSpanBsTbl(models.Model):
    cktspanbsid = models.BigIntegerField()
    cktnodeid = models.IntegerField(blank=True, null=True)
    cktuniqueid = models.IntegerField(blank=True, null=True)
    cktlinkid = models.IntegerField(blank=True, null=True)
    span_type = models.IntegerField()
    cktspansrcctpaccessid = models.BigIntegerField(blank=True, null=True)
    cktspandstctpaccessid = models.BigIntegerField(blank=True, null=True)
    cktspansrcstate = models.NullBooleanField()
    cktspandeststate = models.NullBooleanField()
    iscktforwarding = models.NullBooleanField()
    iscktspaninupsr = models.NullBooleanField()
    iscktspanworking = models.NullBooleanField()
    iscktspanactive = models.NullBooleanField()
    cktspanprotop = models.NullBooleanField()
    cktspancdlflowid = models.IntegerField(blank=True, null=True)
    cktspansrcportname = models.CharField(max_length=64, blank=True, null=True)
    cktspandestportname = models.CharField(max_length=64, blank=True, null=True)
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)
    cktupsrspansrcstate = models.IntegerField(blank=True, null=True)
    cktupsrspandststate = models.IntegerField(blank=True, null=True)
    isinternalspan = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'circuit_span_bs_tbl'


class CircuitSpanTbl(models.Model):
    cktspanid = models.IntegerField()
    cktnodeid = models.IntegerField(blank=True, null=True)
    cktuniqueid = models.IntegerField(blank=True, null=True)
    cktlinkid = models.IntegerField(blank=True, null=True)
    cktspansrcnodeid = models.IntegerField(blank=True, null=True)
    cktspansrcmoduletype = models.IntegerField(blank=True, null=True)
    cktspansrcifindex = models.BigIntegerField(blank=True, null=True)
    cktspansrcobjecttype = models.IntegerField(blank=True, null=True)
    cktspansrcphysicalloc = models.BigIntegerField(blank=True, null=True)
    cktspansrcmodeltype = models.IntegerField(blank=True, null=True)
    cktspandestnodeid = models.IntegerField(blank=True, null=True)
    cktspandestmoduletype = models.IntegerField(blank=True, null=True)
    cktspandestifindex = models.BigIntegerField(blank=True, null=True)
    cktspandestobjecttype = models.IntegerField(blank=True, null=True)
    cktspandestphysicalloc = models.BigIntegerField(blank=True, null=True)
    cktspandestmodeltype = models.IntegerField(blank=True, null=True)
    cktspansrcstate = models.NullBooleanField()
    cktspandeststate = models.NullBooleanField()
    iscktforwarding = models.NullBooleanField()
    iscktspaninupsr = models.NullBooleanField()
    iscktspanworking = models.NullBooleanField()
    iscktspanactive = models.NullBooleanField()
    cktspanprotop = models.NullBooleanField()
    cktspanadditionalinfo = models.CharField(max_length=64, blank=True, null=True)
    cktspancdlflowid = models.IntegerField(blank=True, null=True)
    cktspansrcportname = models.CharField(max_length=64, blank=True, null=True)
    cktspandestportname = models.CharField(max_length=64, blank=True, null=True)
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_span_tbl'


class CircuitTbl(models.Model):
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    cktname = models.CharField(max_length=64, blank=True, null=True)
    cktdescription = models.CharField(max_length=256, blank=True, null=True)
    customerid = models.CharField(max_length=256, blank=True, null=True)
    serviceid = models.CharField(max_length=256, blank=True, null=True)
    ckttype = models.IntegerField(blank=True, null=True)
    cktsize = models.IntegerField(blank=True, null=True)
    cktdirection = models.NullBooleanField()
    cktismonitor = models.NullBooleanField()
    cktstate = models.IntegerField(blank=True, null=True)
    cktenhancedstate = models.IntegerField(blank=True, null=True)
    cktprotectiontype = models.IntegerField(blank=True, null=True)
    cktsrcnodeid = models.IntegerField(blank=True, null=True)
    cktsrcmoduletype = models.IntegerField(blank=True, null=True)
    cktsrcifindex = models.BigIntegerField(blank=True, null=True)
    cktsrcobjecttype = models.IntegerField(blank=True, null=True)
    cktsrcphysicalloc = models.BigIntegerField(blank=True, null=True)
    cktsrcmodeltype = models.IntegerField(blank=True, null=True)
    cktsrcdropprot = models.NullBooleanField()
    cktsrcdropprottype = models.NullBooleanField()
    cktsecsrcnodeid = models.IntegerField(blank=True, null=True)
    cktsecsrcmoduletype = models.IntegerField(blank=True, null=True)
    cktsecsrcifindex = models.BigIntegerField(blank=True, null=True)
    cktsecsrcobjecttype = models.IntegerField(blank=True, null=True)
    cktsecsrcphysicalloc = models.BigIntegerField(blank=True, null=True)
    cktsecsrcmodeltype = models.IntegerField(blank=True, null=True)
    cktsecsrcdropprot = models.NullBooleanField()
    cktsecsrcdropprottype = models.NullBooleanField()
    cktadditionalinfo = models.CharField(max_length=64, blank=True, null=True)
    cktdestnodename = models.CharField(max_length=4000, blank=True, null=True)
    cktdestmodulename = models.CharField(max_length=4000, blank=True, null=True)
    cktdestphysicalloc = models.CharField(max_length=4000, blank=True, null=True)
    cktdestmodeltype = models.CharField(max_length=4000, blank=True, null=True)
    cktdestifindex = models.CharField(max_length=4000, blank=True, null=True)
    cktdestobjecttype = models.CharField(max_length=4000, blank=True, null=True)
    cktcomment = models.CharField(max_length=2014, blank=True, null=True)
    cktsrcportname = models.CharField(max_length=64, blank=True, null=True)
    cktsecsrcportname = models.CharField(max_length=64, blank=True, null=True)
    cktdestportname = models.CharField(max_length=4000, blank=True, null=True)
    cktuselap = models.NullBooleanField()
    cktochncchannel = models.IntegerField(blank=True, null=True)
    cktochncdir = models.NullBooleanField()
    isduplicatename = models.NullBooleanField()
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)
    cktaliasname = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_tbl'
        unique_together = (('cktnodeid', 'cktuniqueid'),)


class CircuitUpsrBsTbl(models.Model):
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    nodeid = models.IntegerField()
    workingctpifindex = models.BigIntegerField()
    workingctpphysicalloc = models.BigIntegerField()
    protectctpifindex = models.BigIntegerField()
    protectctpphysicalloc = models.BigIntegerField()
    currentisworking = models.IntegerField()
    switchstate = models.IntegerField()
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_upsr_bs_tbl'


class CircuitVcgTbl(models.Model):
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    parentcktnodeid = models.IntegerField()
    parentcktuniqueid = models.IntegerField()
    vcgdirection = models.NullBooleanField()
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)
    vcatstate = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'circuit_vcg_tbl'


class CircuitVlanTbl(models.Model):
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    cktvlanid = models.IntegerField()
    cktvlanname = models.CharField(max_length=64, blank=True, null=True)
    npid = models.ForeignKey('NetworkPartitionTable', db_column='npid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit_vlan_tbl'
        unique_together = (('cktnodeid', 'cktuniqueid', 'cktvlanid'),)


class ClisessionCommandHistoryTbl(models.Model):
    sessiontag = models.CharField(max_length=32)
    username = models.ForeignKey('UserTable', db_column='username')
    command_histroy = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'clisession_command_history_tbl'


class ComAuditTrail(models.Model):
    aud_user = models.CharField(max_length=100)
    aud_client_ip = models.CharField(max_length=100)
    aud_server_ip = models.CharField(max_length=100)
    aud_resource = models.CharField(max_length=100)
    aud_action = models.CharField(max_length=100)
    applic_cd = models.CharField(max_length=5)
    aud_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'com_audit_trail'
        unique_together = (('aud_user', 'aud_client_ip', 'aud_server_ip', 'aud_resource', 'aud_action', 'applic_cd', 'aud_date'),)


class ComStatistics(models.Model):
    stat_server_ip = models.CharField(max_length=100)
    stat_date = models.DateField()
    applic_cd = models.CharField(max_length=5)
    stat_precision = models.CharField(max_length=6)
    stat_count = models.FloatField()
    stat_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'com_statistics'
        unique_together = (('stat_server_ip', 'stat_date', 'applic_cd', 'stat_precision', 'stat_name'),)


class ConfigPurgingNedbTable(models.Model):
    tablename = models.CharField(max_length=64)
    type = models.CharField(max_length=5)
    included = models.CharField(max_length=1)
    column_name = models.CharField(max_length=64)
    ne_type = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'config_purging_nedb_table'


class ConnlessTpTable(models.Model):
    cltp_ne_db = models.ForeignKey('MatrixFlowDomainTable')
    cltp_phys_loc = models.BigIntegerField()
    cltp_if_index = models.BigIntegerField()
    cltp_transm_params = models.CharField(max_length=512, blank=True, null=True)
    mfd_native_name = models.ForeignKey('MatrixFlowDomainTable', db_column='mfd_native_name', blank=True, null=True)
    cltp_port_tp_role_state = models.NullBooleanField()
    cltp_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'connless_tp_table'
        unique_together = (('cltp_ne_db_id', 'cltp_phys_loc'),)


class CorbaGwActiveUserTable(models.Model):
    active_session_id = models.CharField(primary_key=True, max_length=128)
    user_name = models.ForeignKey('OssCorbaUserTable', db_column='user_name')
    client_end_ip = models.IntegerField()
    lastlogintime = models.DateField(blank=True, null=True)
    client_end_ipv6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_ipv6 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'corba_gw_active_user_table'


class CountersMappingTable(models.Model):
    counter_id = models.IntegerField(blank=True, null=True)
    countertype = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counters_mapping_table'


class CpoLink(models.Model):
    alias = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    first_tp = models.CharField(max_length=255)
    layer = models.IntegerField()
    second_tp = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    protection = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    id = models.ForeignKey('Netmanagedobject', db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'cpo_link'


class CpoXc(models.Model):
    nedbaccessid = models.IntegerField()
    xcindex = models.IntegerField()
    xclayer = models.IntegerField()
    adminstate = models.IntegerField(blank=True, null=True)
    xcname = models.CharField(max_length=765, blank=True, null=True)
    servicestate = models.IntegerField(blank=True, null=True)
    xcsize = models.IntegerField(blank=True, null=True)
    xctype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpo_xc'


class CrsEnetPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    rxtotalbytes = models.BigIntegerField(blank=True, null=True)
    rxgoodbytes = models.BigIntegerField(blank=True, null=True)
    rxtotalframes = models.BigIntegerField(blank=True, null=True)
    rx8021qframes = models.BigIntegerField(blank=True, null=True)
    rxpauseframes = models.BigIntegerField(blank=True, null=True)
    rxunknownopcodes = models.BigIntegerField(blank=True, null=True)
    rxtot164octetframes = models.BigIntegerField(blank=True, null=True)
    rxtotoctetframesfrom65to127 = models.BigIntegerField(blank=True, null=True)
    rxtotoctetframesfrom128to255 = models.BigIntegerField(blank=True, null=True)
    rxtotoctetframesfrom256to511 = models.BigIntegerField(blank=True, null=True)
    rxtotoctetframesfrom512to1023 = models.BigIntegerField(blank=True, null=True)
    rxtotoctetframesfrom1024to1518 = models.BigIntegerField(blank=True, null=True)
    rxtotoctetframesfrom1519tomax = models.BigIntegerField(blank=True, null=True)
    rxgoodframes = models.BigIntegerField(blank=True, null=True)
    rxunicastframes = models.BigIntegerField(blank=True, null=True)
    rxmulticastframes = models.BigIntegerField(blank=True, null=True)
    rxbroadcastframes = models.BigIntegerField(blank=True, null=True)
    numofbufferoverrunpktsdropped = models.BigIntegerField(blank=True, null=True)
    numofabortedpacketsdropped = models.BigIntegerField(blank=True, null=True)
    numofinvalidvlan_idpktsdropped = models.BigIntegerField(blank=True, null=True)
    invaliddestmacdroppackets = models.BigIntegerField(blank=True, null=True)
    invalidencapdroppackets = models.BigIntegerField(blank=True, null=True)
    numberofmiscpktsdropped = models.BigIntegerField(blank=True, null=True)
    droppedgiantpktsgreaterthanmru = models.BigIntegerField(blank=True, null=True)
    droppedetherstatsundersizepkts = models.BigIntegerField(blank=True, null=True)
    droppedjabberspktsgreatermru = models.BigIntegerField(blank=True, null=True)
    droppedetherstatsfragments = models.BigIntegerField(blank=True, null=True)
    droppedpktswithcrcalignerrors = models.BigIntegerField(blank=True, null=True)
    etherstatscollisions = models.BigIntegerField(blank=True, null=True)
    symbolerrors = models.BigIntegerField(blank=True, null=True)
    droppedmiscerrorpackets = models.BigIntegerField(blank=True, null=True)
    rfc2819ethstatsoversizedpkts = models.BigIntegerField(blank=True, null=True)
    rfc2819ethstatsjabbers = models.BigIntegerField(blank=True, null=True)
    rfc2819ethstatscrcalignerrors = models.BigIntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    rfc3635dot3statsalignerrors = models.BigIntegerField(blank=True, null=True)
    totalbytestransmitted = models.BigIntegerField(blank=True, null=True)
    totalgoodbytestransmitted = models.BigIntegerField(blank=True, null=True)
    totalframestransmitted = models.BigIntegerField(blank=True, null=True)
    tx8021qframes = models.BigIntegerField(blank=True, null=True)
    txtotpauseframes = models.BigIntegerField(blank=True, null=True)
    txtot64octetframes = models.BigIntegerField(blank=True, null=True)
    txtotoctframesfrom65to127 = models.BigIntegerField(blank=True, null=True)
    txtotoctframesfrom128to255 = models.BigIntegerField(blank=True, null=True)
    txtotoctframesfrom256to511 = models.BigIntegerField(blank=True, null=True)
    txtotoctframesfrom512to1023 = models.BigIntegerField(blank=True, null=True)
    txtotoctframesfrom1024to1518 = models.BigIntegerField(blank=True, null=True)
    txtotoctframesfrom1518tomax = models.BigIntegerField(blank=True, null=True)
    txgoodframes = models.BigIntegerField(blank=True, null=True)
    txunicastframes = models.BigIntegerField(blank=True, null=True)
    txmulticastframes = models.BigIntegerField(blank=True, null=True)
    txbroadcastframes = models.BigIntegerField(blank=True, null=True)
    bufferunderrunpacketdrops = models.BigIntegerField(blank=True, null=True)
    abortedpacketdrops = models.BigIntegerField(blank=True, null=True)
    uncounteddroppedframes = models.BigIntegerField(blank=True, null=True)
    miscellaneousoutputerrors = models.BigIntegerField(blank=True, null=True)
    statslinelastclearedtime = models.DateField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crs_enet_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class CtcModelConstTable(models.Model):
    ctcpackagename = models.CharField(max_length=45, blank=True, null=True)
    ctcmodel = models.CharField(max_length=40, blank=True, null=True)
    ctmmodel = models.CharField(max_length=128, blank=True, null=True)
    ctmobjectindex = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_model_const_table'


class CtcUserprofileTable(models.Model):
    userid = models.CharField(primary_key=True, max_length=64)
    userpassword = models.CharField(max_length=64)
    privilegeid = models.ForeignKey('Ons15454PrivilegeTable', db_column='privilegeid')
    userdesc = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_userprofile_table'


class CtmConfigTable(models.Model):
    sectionname = models.CharField(max_length=40)
    propertyname = models.CharField(max_length=40)
    activevalue = models.CharField(max_length=256, blank=True, null=True)
    ispermanent = models.BooleanField()
    permanentvalue = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctm_config_table'
        unique_together = (('sectionname', 'propertyname'),)


class CtmUniqueObjecttypeTable(models.Model):
    objecttype = models.IntegerField(unique=True)
    objectname = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'ctm_unique_objecttype_table'


class CtmUnknownUserTable(models.Model):
    ipaddress = models.IntegerField(primary_key=True)
    failedattempts = models.IntegerField(blank=True, null=True)
    lastloginfailtime = models.DateField(blank=True, null=True)
    lockedstate = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ctm_unknown_user_table'


class CtpSnapshotNesTable(models.Model):
    snapshot = models.ForeignKey('CtpSnapshotTable')
    ipaddressstring = models.CharField(max_length=765, blank=True, null=True)
    name = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctp_snapshot_nes_table'


class CtpSnapshotTable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    collectiondate = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=765)
    status = models.CharField(max_length=765, blank=True, null=True)
    username = models.CharField(max_length=765, blank=True, null=True)
    xmlfile = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctp_snapshot_table'


class CustomViewConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    matcher = models.CharField(max_length=765, blank=True, null=True)
    name = models.CharField(max_length=765, blank=True, null=True)
    report = models.CharField(max_length=765, blank=True, null=True)
    visibility = models.CharField(max_length=765, blank=True, null=True)
    userid = models.ForeignKey('UserTable', db_column='userid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_view_config'


class CustomViewTable(models.Model):
    viewid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey('UserTable', db_column='userid')
    tableid = models.ForeignKey(CMetadata, db_column='tableid')

    class Meta:
        managed = False
        db_table = 'custom_view_table'
        unique_together = (('userid', 'tableid'),)


class DbAuditingTable(models.Model):
    operationid = models.ForeignKey('DbOperationidTable', db_column='operationid', blank=True, null=True)
    op_date = models.DateTimeField()
    status = models.CharField(max_length=32)
    description = models.CharField(max_length=4000)
    additional_info = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_auditing_table'


class DbConnectionConfigTable(models.Model):
    server_id = models.CharField(max_length=256)
    initialimit = models.IntegerField()
    minlimit = models.IntegerField()
    maxlimit = models.IntegerField()
    maxstatmlimit = models.IntegerField()
    inactivity_tmo = models.IntegerField()
    abandoned_tmo = models.IntegerField()
    connect_wait_tmo = models.IntegerField()
    property_check_interval = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'db_connection_config_table'


class DbHistoryTable(models.Model):
    operationid = models.ForeignKey('DbOperationidTable', db_column='operationid', blank=True, null=True)
    op_date = models.DateTimeField()
    starting_version = models.CharField(max_length=32, blank=True, null=True)
    final_version = models.CharField(max_length=32, blank=True, null=True)
    starting_size = models.CharField(max_length=32, blank=True, null=True)
    final_size = models.CharField(max_length=32, blank=True, null=True)
    starting_modules = models.CharField(max_length=32, blank=True, null=True)
    final_modules = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    additional_info = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_history_table'


class DbOperationidTable(models.Model):
    operationid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'db_operationid_table'


class DbPruningTable(models.Model):
    dbprocedure = models.CharField(max_length=32)
    configproperty = models.CharField(max_length=32)
    monitorparam = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'db_pruning_table'


class DbTraceDebugTable(models.Model):
    module = models.CharField(max_length=70)
    level_trace = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'db_trace_debug_table'


class DebugModuleMappingTable(models.Model):
    packageorclass = models.CharField(max_length=80, blank=True, null=True)
    moduleid = models.ForeignKey('DebugModuleTable', db_column='moduleid')

    class Meta:
        managed = False
        db_table = 'debug_module_mapping_table'


class DebugModuleTable(models.Model):
    moduleid = models.IntegerField(primary_key=True)
    modulename = models.CharField(max_length=40, blank=True, null=True)
    configproperty = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debug_module_table'


class DefaultPermissionTable(models.Model):
    operationid = models.ForeignKey('OperationsTable', db_column='operationid')
    userrole = models.BooleanField()
    defaultvalue = models.NullBooleanField()
    editable = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'default_permission_table'
        unique_together = (('operationid', 'userrole'),)


class DeletedUserTable(models.Model):
    username = models.CharField(max_length=64, blank=True, null=True)
    deletedtime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deleted_user_table'


class DiskspaceUsageTable(models.Model):
    partitionname = models.IntegerField()
    usage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diskspace_usage_table'


class DmmChangenotificationconfig(models.Model):
    classid = models.IntegerField(primary_key=True)
    app_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_changenotificationconfig'


class DmmDynamicgrouprule(models.Model):
    instanceid = models.BigIntegerField(primary_key=True)
    rule_type = models.CharField(max_length=765)
    membertype = models.CharField(max_length=765)
    aliasname = models.CharField(max_length=765)
    whereclause = models.TextField(blank=True, null=True)
    groupid = models.ForeignKey('DmmGroup', db_column='groupid')
    startrow = models.IntegerField(blank=True, null=True)
    pagesize = models.IntegerField(blank=True, null=True)
    retrievalspecdepth = models.IntegerField(blank=True, null=True)
    returntotalrowcount = models.NullBooleanField()
    notifyretrievedpages = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'dmm_dynamicgrouprule'


class DmmExcludeassociation(models.Model):
    classid = models.IntegerField()
    associationame = models.CharField(max_length=765)

    class Meta:
        managed = False
        db_table = 'dmm_excludeassociation'
        unique_together = (('classid', 'associationame'),)


class DmmGroup(models.Model):
    instanceid = models.BigIntegerField(primary_key=True)
    group_type = models.CharField(max_length=765)
    instancename = models.CharField(unique=True, max_length=765)
    description = models.CharField(max_length=765, blank=True, null=True)
    userid = models.CharField(max_length=765, blank=True, null=True)
    isstatic = models.CharField(max_length=3, blank=True, null=True)
    notificationtaskid = models.ForeignKey('DmmGroupnotificationtask', db_column='notificationtaskid', blank=True, null=True)
    expirationdate = models.DateField(blank=True, null=True)
    queuename = models.CharField(max_length=765, blank=True, null=True)
    valid = models.NullBooleanField()
    unsubscribe = models.NullBooleanField()
    totalrowcount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_group'


class DmmGroupingroup(models.Model):
    childid = models.ForeignKey(DmmGroup, db_column='childid')
    parentid = models.ForeignKey(DmmGroup, db_column='parentid')

    class Meta:
        managed = False
        db_table = 'dmm_groupingroup'


class DmmGroupmembers(models.Model):
    groupid = models.ForeignKey(DmmGroup, db_column='groupid')
    memberid = models.BigIntegerField()
    membertype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dmm_groupmembers'
        unique_together = (('groupid', 'memberid', 'membertype'),)


class DmmGroupnotificationtask(models.Model):
    instanceid = models.BigIntegerField(primary_key=True)
    queuename = models.CharField(max_length=765)
    grouptype = models.CharField(max_length=765)
    status = models.CharField(max_length=765, blank=True, null=True)
    startrow = models.BigIntegerField(blank=True, null=True)
    endrow = models.BigIntegerField(blank=True, null=True)
    errorcount = models.IntegerField(blank=True, null=True)
    errordate = models.DateTimeField(blank=True, null=True)
    valid = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'dmm_groupnotificationtask'


class DmmModelclass(models.Model):
    classid = models.IntegerField(primary_key=True)
    classname = models.CharField(unique=True, max_length=3072)
    identifiername = models.CharField(max_length=765, blank=True, null=True)
    naturalidname = models.CharField(max_length=765, blank=True, null=True)
    tablename = models.CharField(max_length=765, blank=True, null=True)
    primarykeyname = models.CharField(max_length=765, blank=True, null=True)
    businesskeyname = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_modelclass'


class DmmNotificationbinding(models.Model):
    instanceid = models.BigIntegerField(primary_key=True)
    valid = models.NullBooleanField()
    unsubscribe = models.NullBooleanField()
    queuename = models.CharField(max_length=765)
    groupid = models.ForeignKey(DmmGroup, db_column='groupid')
    startrow = models.IntegerField(blank=True, null=True)
    pagesize = models.IntegerField(blank=True, null=True)
    retrievalspecdepth = models.IntegerField(blank=True, null=True)
    returntotalrowcount = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_notificationbinding'


class DmmPrivilege(models.Model):
    id = models.BigIntegerField(primary_key=True)
    privilegetype = models.CharField(unique=True, max_length=765)

    class Meta:
        managed = False
        db_table = 'dmm_privilege'


class DmmPrunestatus(models.Model):
    app = models.CharField(primary_key=True, max_length=765)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    nextstarttime = models.DateTimeField(blank=True, null=True)
    prunerunning = models.NullBooleanField()
    pruneinterval = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_prunestatus'


class DmmPruningservicedata(models.Model):
    instanceid = models.BigIntegerField(primary_key=True)
    classname = models.CharField(max_length=765, blank=True, null=True)
    tablename = models.CharField(max_length=765, blank=True, null=True)
    prunebytable = models.CharField(max_length=3, blank=True, null=True)
    alias = models.CharField(max_length=765, blank=True, null=True)
    whereclause = models.CharField(max_length=4000, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    maxrecords = models.IntegerField(blank=True, null=True)
    ageattribute = models.CharField(max_length=765, blank=True, null=True)
    batchsize = models.IntegerField(blank=True, null=True)
    pruneorder = models.IntegerField(blank=True, null=True)
    enable = models.NullBooleanField()
    partitionoperation = models.IntegerField(blank=True, null=True)
    partitionclass = models.CharField(max_length=2400, blank=True, null=True)
    partitionname = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_pruningservicedata'


class DmmReport(models.Model):
    reportid = models.BigIntegerField(primary_key=True)
    expirydate = models.DateTimeField(blank=True, null=True)
    queryexecutiontime = models.DateTimeField(blank=True, null=True)
    countcompleted = models.IntegerField(blank=True, null=True)
    totalcount = models.IntegerField(blank=True, null=True)
    reportdefinitionid = models.ForeignKey('DmmReportdefinition', db_column='reportdefinitionid')

    class Meta:
        managed = False
        db_table = 'dmm_report'


class DmmReportdata(models.Model):
    reportid = models.BigIntegerField()
    recordnumber = models.IntegerField()
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_reportdata'
        unique_together = (('reportid', 'recordnumber'),)


class DmmReportdefinition(models.Model):
    reportdefinitionid = models.BigIntegerField(primary_key=True)
    reportname = models.CharField(unique=True, max_length=765, blank=True, null=True)
    query = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_reportdefinition'


class DmmRetrievalspec(models.Model):
    instanceid = models.BigIntegerField(primary_key=True)
    classid = models.IntegerField()
    dynamicgroupruleid = models.ForeignKey(DmmDynamicgrouprule, db_column='dynamicgroupruleid', blank=True, null=True)
    notificationbindingid = models.ForeignKey(DmmNotificationbinding, db_column='notificationbindingid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_retrievalspec'


class DmmRetrievalspecproperties(models.Model):
    instanceid = models.BigIntegerField(primary_key=True)
    propertyname = models.CharField(max_length=765)
    retrievalspecid = models.ForeignKey(DmmRetrievalspec, db_column='retrievalspecid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_retrievalspecproperties'


class DmmRole(models.Model):
    id = models.BigIntegerField(primary_key=True)
    instancename = models.CharField(unique=True, max_length=765)

    class Meta:
        managed = False
        db_table = 'dmm_role'


class DmmRolePrivilege(models.Model):
    roleid = models.ForeignKey(DmmRole, db_column='roleid')
    privilegeid = models.ForeignKey(DmmPrivilege, db_column='privilegeid')

    class Meta:
        managed = False
        db_table = 'dmm_role_privilege'
        unique_together = (('roleid', 'privilegeid'),)


class DmmRolegroup(models.Model):
    sourcegroupid = models.ForeignKey(DmmGroup, db_column='sourcegroupid')
    targetgroupid = models.ForeignKey(DmmGroup, db_column='targetgroupid')
    roleid = models.ForeignKey(DmmRole, db_column='roleid')

    class Meta:
        managed = False
        db_table = 'dmm_rolegroup'
        unique_together = (('sourcegroupid', 'targetgroupid', 'roleid'),)


class DmmSyncgroupmembertype(models.Model):
    instanceid = models.BigIntegerField(primary_key=True)
    groupid = models.ForeignKey(DmmGroup, db_column='groupid')
    membertype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_syncgroupmembertype'


class DmmTransactionalqueue(models.Model):
    instanceid = models.BigIntegerField()
    classid = models.IntegerField(blank=True, null=True)
    operation = models.CharField(max_length=21, blank=True, null=True)
    changedip = models.BigIntegerField(blank=True, null=True)
    propertyvalue = models.CharField(max_length=4000, blank=True, null=True)
    createdtime = models.DateTimeField(blank=True, null=True)
    partitionno = models.IntegerField(blank=True, null=True)
    workflowid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_transactionalqueue'


class DmmTrxqueuescanposition(models.Model):
    scannername = models.CharField(primary_key=True, max_length=765)
    scanposition = models.BigIntegerField(blank=True, null=True)
    partitionno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmm_trxqueuescanposition'


class DockingConfTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dockedheight = models.IntegerField()
    dockedside = models.CharField(max_length=255, blank=True, null=True)
    dockedwidth = models.IntegerField()
    floatingwidth = models.IntegerField()
    floatingx = models.IntegerField()
    floatingy = models.IntegerField()
    floatingheight = models.IntegerField()
    docking_index = models.IntegerField()
    docking_name = models.CharField(max_length=765, blank=True, null=True)
    state = models.CharField(max_length=765, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    ishidden = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'docking_conf_table'
        unique_together = (('user_id', 'docking_name'),)


class DomainTable(models.Model):
    treenodeid = models.IntegerField()
    parenttype = models.IntegerField()
    parentid = models.IntegerField()
    childtype = models.IntegerField()
    childid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'domain_table'
        unique_together = (('parenttype', 'parentid', 'childtype', 'childid'),)


class DummyTable(models.Model):
    phyloc = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dummy_table'


class EmsAlarmTable(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    alarmindex = models.IntegerField()
    isgroup = models.BooleanField()
    severity = models.NullBooleanField()
    isenabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ems_alarm_table'
        unique_together = (('alarmindex', 'isgroup'),)


class EmsAlarmTableTemp(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    alarmindex = models.IntegerField(blank=True, null=True)
    isgroup = models.NullBooleanField()
    severity = models.NullBooleanField()
    isenabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ems_alarm_table_temp'


class EnumMapTable(models.Model):
    clazz = models.CharField(max_length=765)
    enumlabel = models.CharField(max_length=765)
    enumvalue = models.IntegerField()
    locale = models.CharField(max_length=765)
    displaylabel = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enum_map_table'
        unique_together = (('clazz', 'enumlabel', 'enumvalue', 'locale'),)


class EnumTable(models.Model):
    enumbase = models.IntegerField()
    enumint = models.IntegerField()
    uivalue = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enum_table'
        unique_together = (('enumbase', 'enumint'),)


class EqptInfoTable(models.Model):
    nedbaccessid = models.IntegerField()
    physicalloc = models.BigIntegerField()
    ifindex = models.BigIntegerField()
    moduletype = models.IntegerField()
    objectindex = models.IntegerField()
    modeltype = models.IntegerField()
    strobjinstance = models.CharField(max_length=256)
    col1 = models.CharField(max_length=256, blank=True, null=True)
    col2 = models.CharField(max_length=256, blank=True, null=True)
    col3 = models.CharField(max_length=256, blank=True, null=True)
    col4 = models.CharField(max_length=256, blank=True, null=True)
    col5 = models.CharField(max_length=256, blank=True, null=True)
    col6 = models.CharField(max_length=256, blank=True, null=True)
    col7 = models.CharField(max_length=256, blank=True, null=True)
    col8 = models.CharField(max_length=256, blank=True, null=True)
    col9 = models.CharField(max_length=256, blank=True, null=True)
    col10 = models.CharField(max_length=256, blank=True, null=True)
    col11 = models.CharField(max_length=256, blank=True, null=True)
    col12 = models.CharField(max_length=256, blank=True, null=True)
    col13 = models.CharField(max_length=256, blank=True, null=True)
    col14 = models.CharField(max_length=256, blank=True, null=True)
    col15 = models.CharField(max_length=256, blank=True, null=True)
    col16 = models.CharField(max_length=256, blank=True, null=True)
    col17 = models.CharField(max_length=256, blank=True, null=True)
    col18 = models.CharField(max_length=256, blank=True, null=True)
    col19 = models.CharField(max_length=256, blank=True, null=True)
    col20 = models.CharField(max_length=256, blank=True, null=True)
    col21 = models.CharField(max_length=256, blank=True, null=True)
    col22 = models.CharField(max_length=256, blank=True, null=True)
    col23 = models.CharField(max_length=256, blank=True, null=True)
    col24 = models.CharField(max_length=256, blank=True, null=True)
    col25 = models.CharField(max_length=256, blank=True, null=True)
    col26 = models.CharField(max_length=256, blank=True, null=True)
    col27 = models.CharField(max_length=256, blank=True, null=True)
    col28 = models.CharField(max_length=256, blank=True, null=True)
    col29 = models.CharField(max_length=256, blank=True, null=True)
    col30 = models.CharField(max_length=256, blank=True, null=True)
    col31 = models.CharField(max_length=256, blank=True, null=True)
    col32 = models.CharField(max_length=256, blank=True, null=True)
    col33 = models.CharField(max_length=256, blank=True, null=True)
    col34 = models.CharField(max_length=256, blank=True, null=True)
    col35 = models.CharField(max_length=256, blank=True, null=True)
    col36 = models.CharField(max_length=256, blank=True, null=True)
    col37 = models.CharField(max_length=256, blank=True, null=True)
    col38 = models.CharField(max_length=256, blank=True, null=True)
    col39 = models.CharField(max_length=256, blank=True, null=True)
    col40 = models.CharField(max_length=256, blank=True, null=True)
    col41 = models.CharField(max_length=256, blank=True, null=True)
    col42 = models.CharField(max_length=256, blank=True, null=True)
    col43 = models.CharField(max_length=256, blank=True, null=True)
    col44 = models.CharField(max_length=256, blank=True, null=True)
    col45 = models.CharField(max_length=256, blank=True, null=True)
    col46 = models.CharField(max_length=256, blank=True, null=True)
    col47 = models.CharField(max_length=256, blank=True, null=True)
    col48 = models.CharField(max_length=256, blank=True, null=True)
    col49 = models.CharField(max_length=256, blank=True, null=True)
    col50 = models.CharField(max_length=256, blank=True, null=True)
    col51 = models.CharField(max_length=256, blank=True, null=True)
    col52 = models.CharField(max_length=256, blank=True, null=True)
    col53 = models.CharField(max_length=256, blank=True, null=True)
    col54 = models.CharField(max_length=256, blank=True, null=True)
    col55 = models.CharField(max_length=256, blank=True, null=True)
    col56 = models.CharField(max_length=256, blank=True, null=True)
    col57 = models.CharField(max_length=256, blank=True, null=True)
    col58 = models.CharField(max_length=256, blank=True, null=True)
    col59 = models.CharField(max_length=256, blank=True, null=True)
    col60 = models.CharField(max_length=256, blank=True, null=True)
    col61 = models.CharField(max_length=256, blank=True, null=True)
    col62 = models.CharField(max_length=256, blank=True, null=True)
    col63 = models.CharField(max_length=256, blank=True, null=True)
    col64 = models.CharField(max_length=256, blank=True, null=True)
    col65 = models.CharField(max_length=256, blank=True, null=True)
    col66 = models.CharField(max_length=256, blank=True, null=True)
    col67 = models.CharField(max_length=256, blank=True, null=True)
    col68 = models.CharField(max_length=256, blank=True, null=True)
    col69 = models.CharField(max_length=256, blank=True, null=True)
    col70 = models.CharField(max_length=256, blank=True, null=True)
    col71 = models.CharField(max_length=256, blank=True, null=True)
    col72 = models.CharField(max_length=256, blank=True, null=True)
    col73 = models.CharField(max_length=256, blank=True, null=True)
    col74 = models.CharField(max_length=256, blank=True, null=True)
    col75 = models.CharField(max_length=256, blank=True, null=True)
    col76 = models.CharField(max_length=256, blank=True, null=True)
    col77 = models.CharField(max_length=256, blank=True, null=True)
    col78 = models.CharField(max_length=256, blank=True, null=True)
    col79 = models.CharField(max_length=256, blank=True, null=True)
    col80 = models.CharField(max_length=256, blank=True, null=True)
    col81 = models.CharField(max_length=256, blank=True, null=True)
    col82 = models.CharField(max_length=256, blank=True, null=True)
    col83 = models.CharField(max_length=256, blank=True, null=True)
    col84 = models.CharField(max_length=256, blank=True, null=True)
    col85 = models.CharField(max_length=256, blank=True, null=True)
    col86 = models.CharField(max_length=256, blank=True, null=True)
    col87 = models.CharField(max_length=256, blank=True, null=True)
    col88 = models.CharField(max_length=256, blank=True, null=True)
    col89 = models.CharField(max_length=256, blank=True, null=True)
    col90 = models.CharField(max_length=256, blank=True, null=True)
    col91 = models.CharField(max_length=256, blank=True, null=True)
    col92 = models.CharField(max_length=256, blank=True, null=True)
    col93 = models.CharField(max_length=256, blank=True, null=True)
    col94 = models.CharField(max_length=256, blank=True, null=True)
    col95 = models.CharField(max_length=256, blank=True, null=True)
    col96 = models.CharField(max_length=256, blank=True, null=True)
    col97 = models.CharField(max_length=256, blank=True, null=True)
    col98 = models.CharField(max_length=256, blank=True, null=True)
    col99 = models.CharField(max_length=256, blank=True, null=True)
    col100 = models.CharField(max_length=256, blank=True, null=True)
    col101 = models.CharField(max_length=256, blank=True, null=True)
    col102 = models.CharField(max_length=256, blank=True, null=True)
    col103 = models.CharField(max_length=256, blank=True, null=True)
    col104 = models.CharField(max_length=256, blank=True, null=True)
    col105 = models.CharField(max_length=256, blank=True, null=True)
    col106 = models.CharField(max_length=256, blank=True, null=True)
    col107 = models.CharField(max_length=256, blank=True, null=True)
    col108 = models.CharField(max_length=256, blank=True, null=True)
    col109 = models.CharField(max_length=256, blank=True, null=True)
    col110 = models.CharField(max_length=256, blank=True, null=True)
    col111 = models.CharField(max_length=256, blank=True, null=True)
    col112 = models.CharField(max_length=256, blank=True, null=True)
    col113 = models.CharField(max_length=256, blank=True, null=True)
    col114 = models.CharField(max_length=256, blank=True, null=True)
    col115 = models.CharField(max_length=256, blank=True, null=True)
    col116 = models.CharField(max_length=256, blank=True, null=True)
    col117 = models.CharField(max_length=256, blank=True, null=True)
    col118 = models.CharField(max_length=256, blank=True, null=True)
    col119 = models.CharField(max_length=256, blank=True, null=True)
    col120 = models.CharField(max_length=256, blank=True, null=True)
    col121 = models.CharField(max_length=256, blank=True, null=True)
    col122 = models.CharField(max_length=256, blank=True, null=True)
    col123 = models.CharField(max_length=256, blank=True, null=True)
    col124 = models.CharField(max_length=256, blank=True, null=True)
    col125 = models.CharField(max_length=256, blank=True, null=True)
    col126 = models.CharField(max_length=256, blank=True, null=True)
    col127 = models.CharField(max_length=256, blank=True, null=True)
    col128 = models.CharField(max_length=256, blank=True, null=True)
    col129 = models.CharField(max_length=256, blank=True, null=True)
    col130 = models.CharField(max_length=256, blank=True, null=True)
    col131 = models.CharField(max_length=256, blank=True, null=True)
    col132 = models.CharField(max_length=256, blank=True, null=True)
    col133 = models.CharField(max_length=256, blank=True, null=True)
    col134 = models.CharField(max_length=256, blank=True, null=True)
    col135 = models.CharField(max_length=256, blank=True, null=True)
    col136 = models.CharField(max_length=256, blank=True, null=True)
    col137 = models.CharField(max_length=256, blank=True, null=True)
    col138 = models.CharField(max_length=256, blank=True, null=True)
    col139 = models.CharField(max_length=256, blank=True, null=True)
    col140 = models.CharField(max_length=256, blank=True, null=True)
    col141 = models.CharField(max_length=256, blank=True, null=True)
    col142 = models.CharField(max_length=256, blank=True, null=True)
    col143 = models.CharField(max_length=256, blank=True, null=True)
    col144 = models.CharField(max_length=256, blank=True, null=True)
    col145 = models.CharField(max_length=256, blank=True, null=True)
    col146 = models.CharField(max_length=256, blank=True, null=True)
    col147 = models.CharField(max_length=256, blank=True, null=True)
    col148 = models.CharField(max_length=256, blank=True, null=True)
    col149 = models.CharField(max_length=256, blank=True, null=True)
    col150 = models.CharField(max_length=256, blank=True, null=True)
    col151 = models.CharField(max_length=256, blank=True, null=True)
    col152 = models.CharField(max_length=256, blank=True, null=True)
    col153 = models.CharField(max_length=256, blank=True, null=True)
    col154 = models.CharField(max_length=256, blank=True, null=True)
    col155 = models.CharField(max_length=256, blank=True, null=True)
    col156 = models.CharField(max_length=256, blank=True, null=True)
    col157 = models.CharField(max_length=256, blank=True, null=True)
    col158 = models.CharField(max_length=256, blank=True, null=True)
    col159 = models.CharField(max_length=256, blank=True, null=True)
    col160 = models.CharField(max_length=256, blank=True, null=True)
    col161 = models.CharField(max_length=256, blank=True, null=True)
    col162 = models.CharField(max_length=256, blank=True, null=True)
    col163 = models.CharField(max_length=256, blank=True, null=True)
    col164 = models.CharField(max_length=256, blank=True, null=True)
    col165 = models.CharField(max_length=256, blank=True, null=True)
    col166 = models.CharField(max_length=256, blank=True, null=True)
    col167 = models.CharField(max_length=256, blank=True, null=True)
    col168 = models.CharField(max_length=256, blank=True, null=True)
    col169 = models.CharField(max_length=256, blank=True, null=True)
    col170 = models.CharField(max_length=256, blank=True, null=True)
    col171 = models.CharField(max_length=256, blank=True, null=True)
    col172 = models.CharField(max_length=256, blank=True, null=True)
    col173 = models.CharField(max_length=256, blank=True, null=True)
    col174 = models.CharField(max_length=256, blank=True, null=True)
    col175 = models.CharField(max_length=256, blank=True, null=True)
    col176 = models.CharField(max_length=256, blank=True, null=True)
    col177 = models.CharField(max_length=256, blank=True, null=True)
    col178 = models.CharField(max_length=256, blank=True, null=True)
    col179 = models.CharField(max_length=256, blank=True, null=True)
    col180 = models.CharField(max_length=256, blank=True, null=True)
    col181 = models.CharField(max_length=256, blank=True, null=True)
    col182 = models.CharField(max_length=256, blank=True, null=True)
    col183 = models.CharField(max_length=256, blank=True, null=True)
    col184 = models.CharField(max_length=256, blank=True, null=True)
    col185 = models.CharField(max_length=256, blank=True, null=True)
    col186 = models.CharField(max_length=256, blank=True, null=True)
    col187 = models.CharField(max_length=256, blank=True, null=True)
    col188 = models.CharField(max_length=256, blank=True, null=True)
    col189 = models.CharField(max_length=256, blank=True, null=True)
    col190 = models.CharField(max_length=256, blank=True, null=True)
    col191 = models.CharField(max_length=256, blank=True, null=True)
    col192 = models.CharField(max_length=256, blank=True, null=True)
    col193 = models.CharField(max_length=256, blank=True, null=True)
    col194 = models.CharField(max_length=256, blank=True, null=True)
    col195 = models.CharField(max_length=256, blank=True, null=True)
    col196 = models.CharField(max_length=256, blank=True, null=True)
    col197 = models.CharField(max_length=256, blank=True, null=True)
    col198 = models.CharField(max_length=256, blank=True, null=True)
    col199 = models.CharField(max_length=256, blank=True, null=True)
    col200 = models.CharField(max_length=256, blank=True, null=True)
    col201 = models.CharField(max_length=256, blank=True, null=True)
    col202 = models.CharField(max_length=256, blank=True, null=True)
    col203 = models.CharField(max_length=256, blank=True, null=True)
    col204 = models.CharField(max_length=256, blank=True, null=True)
    col205 = models.CharField(max_length=256, blank=True, null=True)
    col206 = models.CharField(max_length=256, blank=True, null=True)
    col207 = models.CharField(max_length=256, blank=True, null=True)
    col208 = models.CharField(max_length=256, blank=True, null=True)
    col209 = models.CharField(max_length=256, blank=True, null=True)
    col210 = models.CharField(max_length=256, blank=True, null=True)
    col211 = models.CharField(max_length=256, blank=True, null=True)
    col212 = models.CharField(max_length=256, blank=True, null=True)
    col213 = models.CharField(max_length=256, blank=True, null=True)
    col214 = models.CharField(max_length=256, blank=True, null=True)
    col215 = models.CharField(max_length=256, blank=True, null=True)
    col216 = models.CharField(max_length=256, blank=True, null=True)
    col217 = models.CharField(max_length=256, blank=True, null=True)
    col218 = models.CharField(max_length=256, blank=True, null=True)
    col219 = models.CharField(max_length=256, blank=True, null=True)
    col220 = models.CharField(max_length=256, blank=True, null=True)
    col221 = models.CharField(max_length=256, blank=True, null=True)
    col222 = models.CharField(max_length=256, blank=True, null=True)
    col223 = models.CharField(max_length=256, blank=True, null=True)
    col224 = models.CharField(max_length=256, blank=True, null=True)
    col225 = models.CharField(max_length=256, blank=True, null=True)
    col226 = models.CharField(max_length=256, blank=True, null=True)
    col227 = models.CharField(max_length=256, blank=True, null=True)
    col228 = models.CharField(max_length=256, blank=True, null=True)
    col229 = models.CharField(max_length=256, blank=True, null=True)
    col230 = models.CharField(max_length=256, blank=True, null=True)
    col231 = models.CharField(max_length=256, blank=True, null=True)
    col232 = models.CharField(max_length=256, blank=True, null=True)
    col233 = models.CharField(max_length=256, blank=True, null=True)
    col234 = models.CharField(max_length=256, blank=True, null=True)
    col235 = models.CharField(max_length=256, blank=True, null=True)
    col236 = models.CharField(max_length=256, blank=True, null=True)
    col237 = models.CharField(max_length=256, blank=True, null=True)
    col238 = models.CharField(max_length=256, blank=True, null=True)
    col239 = models.CharField(max_length=256, blank=True, null=True)
    col240 = models.CharField(max_length=256, blank=True, null=True)
    col241 = models.CharField(max_length=256, blank=True, null=True)
    col242 = models.CharField(max_length=256, blank=True, null=True)
    col243 = models.CharField(max_length=256, blank=True, null=True)
    col244 = models.CharField(max_length=256, blank=True, null=True)
    col245 = models.CharField(max_length=256, blank=True, null=True)
    col246 = models.CharField(max_length=256, blank=True, null=True)
    col247 = models.CharField(max_length=256, blank=True, null=True)
    col248 = models.CharField(max_length=4000, blank=True, null=True)
    col249 = models.CharField(max_length=4000, blank=True, null=True)
    col250 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eqpt_info_table'
        unique_together = (('nedbaccessid', 'physicalloc', 'ifindex', 'moduletype', 'objectindex', 'modeltype', 'strobjinstance'),)


class EqptRelationshipTable(models.Model):
    nedbaccessid = models.IntegerField()
    selfphysicalloc = models.BigIntegerField()
    selfifindex = models.BigIntegerField()
    selfmoduletype = models.IntegerField()
    selfmodeltype = models.IntegerField()
    selfobjectindex = models.IntegerField()
    selfstrobjinst = models.CharField(max_length=4000)
    relatedphysicalloc = models.BigIntegerField()
    relatedifindex = models.BigIntegerField()
    relatedmoduletype = models.IntegerField()
    relatedmodeltype = models.IntegerField()
    relatedobjectindex = models.IntegerField()
    relatedstrobjinst = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'eqpt_relationship_table'
        unique_together = (('nedbaccessid', 'selfphysicalloc', 'selfifindex', 'selfmoduletype', 'selfmodeltype', 'selfobjectindex', 'relatedphysicalloc', 'relatedifindex', 'relatedmoduletype', 'relatedmodeltype', 'relatedobjectindex'),)


class ErrorLogTable(models.Model):
    timestamp = models.DateField(blank=True, null=True)
    module = models.IntegerField()
    severity = models.IntegerField()
    submodule = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=256, blank=True, null=True)
    linenumber = models.IntegerField(blank=True, null=True)
    logmessage = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_log_table'


class EvcEfp(models.Model):
    nedbid = models.ForeignKey('MplsServiceTable', db_column='nedbid')
    ptsindex = models.ForeignKey('MplsServiceTable', db_column='ptsindex')
    serviceid = models.ForeignKey('MplsServiceTable', db_column='serviceid')
    ctcindex = models.IntegerField()
    serstate = models.BooleanField()
    isdoubletagged = models.BooleanField()
    isexact = models.BooleanField()
    isstatsenabled = models.BooleanField()
    portdirection = models.BooleanField()
    primaryloadbal = models.IntegerField()
    outvlantag = models.CharField(max_length=256)
    outvlantpid = models.IntegerField()
    invlantag = models.CharField(max_length=256)
    invlantpid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evc_efp'
        unique_together = (('nedbid', 'ptsindex', 'serviceid', 'ctcindex'),)


class EvcEp(models.Model):
    nedbid = models.ForeignKey('MplsServiceTable', db_column='nedbid')
    ptsindex = models.ForeignKey('MplsServiceTable', db_column='ptsindex')
    serviceid = models.ForeignKey('MplsServiceTable', db_column='serviceid')
    ctcindex = models.IntegerField()
    phyloc = models.BigIntegerField()
    ctmuniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    operstate = models.BooleanField()
    adminstate = models.BooleanField()
    linkid = models.IntegerField()
    servicetype = models.IntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)
    slotmoduletype = models.IntegerField()
    portmoduletype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evc_ep'
        unique_together = (('nedbid', 'ptsindex', 'serviceid', 'ctcindex'),)


class EvcNode(models.Model):
    nedbid = models.ForeignKey('MplsServiceTable', db_column='nedbid')
    ptsindex = models.ForeignKey('MplsServiceTable', db_column='ptsindex')
    serviceid = models.ForeignKey('MplsServiceTable', db_column='serviceid')
    ctmuniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    operstate = models.BooleanField()
    adminstate = models.BooleanField()
    servicetype = models.IntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evc_node'
        unique_together = (('nedbid', 'ptsindex', 'serviceid'),)


class EvcPp(models.Model):
    nedbid = models.ForeignKey('MplsServiceTable', db_column='nedbid')
    ptsindex = models.ForeignKey('MplsServiceTable', db_column='ptsindex')
    serviceid = models.ForeignKey('MplsServiceTable', db_column='serviceid')
    ctcindex = models.IntegerField()
    phyloc = models.BigIntegerField()
    ctmuniqid = models.IntegerField()
    linkid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evc_pp'
        unique_together = (('nedbid', 'ptsindex', 'serviceid', 'ctcindex'),)


class EvcSrv(models.Model):
    serviceid = models.IntegerField()
    ctmuniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    discoverystate = models.BooleanField()
    operstate = models.BooleanField()
    epcount = models.IntegerField()
    servicetype = models.IntegerField()
    rxbw = models.BigIntegerField()
    txbw = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'evc_srv'
        unique_together = (('serviceid', 'ctmuniqid'),)


class FilterConfigColumn(models.Model):
    viewid = models.ForeignKey(CustomViewConfig, db_column='viewid')
    attr = models.CharField(max_length=765, blank=True, null=True)
    viewindex = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filter_config_column'
        unique_together = (('viewid', 'position'),)


class FilterConfigRow(models.Model):
    viewid = models.ForeignKey(CustomViewConfig, db_column='viewid')
    attr = models.CharField(max_length=765, blank=True, null=True)
    expectedvalue = models.CharField(max_length=765, blank=True, null=True)
    operator = models.CharField(max_length=765, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filter_config_row'
        unique_together = (('viewid', 'position'),)


class FilterTrial(models.Model):
    table_name = models.CharField(max_length=128)
    filter = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter_trial'


class FkRegenerationTemp(models.Model):
    fk_script = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fk_regeneration_temp'


class FlowDomainTable(models.Model):
    fd_user_label = models.CharField(max_length=64, blank=True, null=True)
    fd_native_name = models.CharField(primary_key=True, max_length=64)
    fd_owner = models.CharField(max_length=64, blank=True, null=True)
    fd_transm_params = models.CharField(max_length=512, blank=True, null=True)
    fd_net_access_domain = models.CharField(max_length=64, blank=True, null=True)
    fd_conn_state = models.NullBooleanField()
    fd_type = models.NullBooleanField()
    fd_additional_info = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow_domain_table'


class GmplsRouteConstrTable(models.Model):
    constr_id = models.IntegerField()
    cktnodeid = models.ForeignKey('GmplsValueTable', db_column='cktnodeid')
    cktuniqueid = models.ForeignKey('GmplsValueTable', db_column='cktuniqueid')
    constraint_ctctype = models.BooleanField()
    constraint_cpotype = models.BooleanField()
    constraint_ctcindex = models.IntegerField()
    constraint_nodeid = models.IntegerField()
    constraint_nedbid = models.IntegerField()
    constraint_path = models.BooleanField()
    constraint_tpmodelkey = models.CharField(max_length=1024, blank=True, null=True)
    constraint_tpmodelname = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmpls_route_constr_table'


class GmplsValueTable(models.Model):
    cktnodeid = models.ForeignKey(CircuitBsTbl, db_column='cktnodeid')
    cktuniqueid = models.ForeignKey(CircuitBsTbl, db_column='cktuniqueid')
    actp_threshold = models.IntegerField()
    actp_restoration_threshold = models.IntegerField()
    actp_protect_threshold = models.IntegerField()
    actp_prot_resto_threshold = models.IntegerField()
    optical_mode = models.IntegerField()
    restoration_optical_mode = models.IntegerField()
    opt_value = models.IntegerField()
    restoration_value = models.IntegerField()
    revertive_value = models.IntegerField()
    soaktime_value = models.IntegerField()
    ignorepathalarm_value = models.BooleanField()
    restorationstate_value = models.IntegerField()
    priority_value = models.IntegerField()
    diversitycktnodeid = models.IntegerField()
    diversitycktuniqueid = models.IntegerField()
    label = models.CharField(max_length=256, blank=True, null=True)
    downstreampoweroffset = models.IntegerField()
    upstreampoweroffset = models.IntegerField()
    isregenallowed = models.BooleanField()
    isuni = models.BooleanField()
    wson_api_level = models.IntegerField()
    current_actp_threshold = models.IntegerField()
    current_opt_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gmpls_value_table'
        unique_together = (('cktnodeid', 'cktuniqueid'),)


class GneTable(models.Model):
    gneid = models.IntegerField(primary_key=True)
    gnetype = models.IntegerField(blank=True, null=True)
    ringid = models.IntegerField(blank=True, null=True)
    gnesysid = models.CharField(max_length=128)
    nedbaccessid = models.IntegerField()
    gnecomment = models.CharField(max_length=512, blank=True, null=True)
    groupoption = models.NullBooleanField()
    groupprefix = models.CharField(max_length=12, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gne_table'


class GroupInfoTable(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(unique=True, max_length=64)
    groupdescription = models.CharField(max_length=256, blank=True, null=True)
    groupuserlabel = models.CharField(max_length=64, blank=True, null=True)
    grouplocationname = models.CharField(max_length=64, blank=True, null=True)
    grouptype = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_info_table'


class GwSnmpOssInfoTable(models.Model):
    snmpv3_username = models.CharField(max_length=64)
    snmpv3_community = models.CharField(max_length=64, blank=True, null=True)
    snmpv3_auth_prot = models.CharField(max_length=64)
    snmpv3_auth_pwd = models.CharField(max_length=64)
    snmpv3_priv_prot = models.CharField(max_length=64)
    snmpv3_priv_pwd = models.CharField(max_length=64)
    snmp_version = models.IntegerField(blank=True, null=True)
    snmp_community = models.CharField(max_length=64, blank=True, null=True)
    snmpv_port = models.IntegerField(blank=True, null=True)
    snmpv3_eid = models.CharField(max_length=64)
    snmpv3_ip = models.TextField()  # This field type is a guess.
    snmpv3_is_ip6 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'gw_snmp_oss_info_table'
        unique_together = (('snmpv3_username', 'snmpv3_auth_prot', 'snmpv3_auth_pwd', 'snmpv3_priv_prot', 'snmpv3_priv_pwd', 'snmpv3_eid', 'snmpv3_ip'),)


class GwcorbaObjectParamMap(models.Model):
    infotype = models.CharField(max_length=16)
    terminationpoint = models.IntegerField()
    layerrate = models.IntegerField()
    attrindex = models.IntegerField()
    metadataindex = models.IntegerField()
    tmfname = models.CharField(max_length=33)
    read = models.BooleanField()
    write = models.BooleanField()
    islocal = models.NullBooleanField()
    featureid = models.CharField(max_length=32, blank=True, null=True)
    objindexmodifier = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    suppmoduletypes = models.CharField(max_length=128, blank=True, null=True)
    paramdefault = models.CharField(max_length=33, blank=True, null=True)
    paramminval = models.CharField(max_length=33, blank=True, null=True)
    parammaxval = models.CharField(max_length=33, blank=True, null=True)
    enumlist = models.CharField(max_length=4000, blank=True, null=True)
    andorprecondition = models.NullBooleanField()
    preconditionlist = models.CharField(max_length=512, blank=True, null=True)
    dbtablepkg = models.CharField(max_length=128, blank=True, null=True)
    dbtablename = models.CharField(max_length=64, blank=True, null=True)
    dbculomnname = models.CharField(max_length=64, blank=True, null=True)
    dbrowcreateval = models.CharField(max_length=33, blank=True, null=True)
    dbrowdeleteval = models.CharField(max_length=33, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwcorba_object_param_map'


class GwcorbaObjectParamTables(models.Model):
    dbtablepkg = models.CharField(max_length=128)
    dbtablename = models.CharField(max_length=64)
    metadataindex = models.IntegerField()
    nedbidcolname = models.CharField(max_length=64, blank=True, null=True)
    moduletypecolname = models.CharField(max_length=64, blank=True, null=True)
    objecttypecolname = models.CharField(max_length=64, blank=True, null=True)
    phyloccolname = models.CharField(max_length=64, blank=True, null=True)
    ifindexcolname = models.CharField(max_length=64, blank=True, null=True)
    defaultcolvalues = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwcorba_object_param_tables'


class GwcorbaPmMappingTable(models.Model):
    modeltype = models.IntegerField()
    layerrate = models.IntegerField()
    objectindex = models.IntegerField()
    location = models.IntegerField()
    direction = models.IntegerField()
    terminationpoint = models.IntegerField()
    pmviewname = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'gwcorba_pm_mapping_table'


class IfCrossConnect(models.Model):
    xcdbaccessid = models.IntegerField()
    nedbaccessid = models.IntegerField()
    srcifdbaccessid = models.ForeignKey('Mib2InterfaceTable', db_column='srcifdbaccessid')
    destifdbaccessid = models.ForeignKey('Mib2InterfaceTable', db_column='destifdbaccessid')
    xctype = models.IntegerField(blank=True, null=True)
    xckind = models.IntegerField(blank=True, null=True)
    creationtime = models.DateField(blank=True, null=True)
    src2destoperstatus = models.IntegerField()
    dest2srcoperstatus = models.IntegerField()
    src2destlastchange = models.DateField(blank=True, null=True)
    dest2srclastchange = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'if_cross_connect'


class IfDwdmChannelGroup(models.Model):
    ifdbaccessid = models.ForeignKey('Mib2InterfaceTable', db_column='ifdbaccessid', primary_key=True)
    nedbaccessid = models.IntegerField()
    minfrequency = models.IntegerField()
    spacing = models.IntegerField()
    bitmaplogic = models.IntegerField(blank=True, null=True)
    bitmap = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'if_dwdm_channel_group'


class IfOpticalPhyConfigTable(models.Model):
    ifdbaccessid = models.IntegerField(primary_key=True)
    nedbaccessid = models.IntegerField()
    ifmode = models.IntegerField(blank=True, null=True)
    ifprotocol = models.IntegerField(blank=True, null=True)
    ifclockrate = models.IntegerField(blank=True, null=True)
    ifmonitorstate = models.NullBooleanField()
    ifloopback = models.IntegerField(blank=True, null=True)
    ifofc = models.NullBooleanField()
    iflasersafteycontrol = models.NullBooleanField()
    ifflc = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'if_optical_phy_config_table'


class IfindexRuleTable(models.Model):
    modeltype = models.IntegerField()
    objecttype = models.IntegerField()
    attributenameconst = models.IntegerField()
    attrorder = models.IntegerField()
    attrsize = models.IntegerField()
    attrtype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ifindex_rule_table'
        unique_together = (('modeltype', 'objecttype', 'attributenameconst'),)


class InterfaceApsInfo(models.Model):
    ifdbaccessid = models.ForeignKey('Mib2InterfaceTable', db_column='ifdbaccessid', primary_key=True)
    nedbaccessid = models.IntegerField()
    apsgroupname = models.CharField(max_length=64, blank=True, null=True)
    apschannumber = models.IntegerField(blank=True, null=True)
    apschanstatuscurrent = models.IntegerField(blank=True, null=True)
    apschanlastswitchover = models.DateField(blank=True, null=True)
    apsinterfacestate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interface_aps_info'


class InterfaceDwdmFrequency(models.Model):
    ifdbaccessid = models.ForeignKey('Mib2InterfaceTable', db_column='ifdbaccessid', primary_key=True)
    nedbaccessid = models.IntegerField()
    frequency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'interface_dwdm_frequency'


class InterfaceStackTable(models.Model):
    uniqueid = models.IntegerField()
    nedbaccessid = models.IntegerField()
    highifdbaccessid = models.ForeignKey('Mib2InterfaceTable', db_column='highifdbaccessid')
    lowifdbaccessid = models.ForeignKey('Mib2InterfaceTable', db_column='lowifdbaccessid')
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'interface_stack_table'
        unique_together = (('highifdbaccessid', 'lowifdbaccessid'),)


class InterfaceTable(models.Model):
    netype = models.BooleanField()
    ifstaticindex = models.IntegerField(primary_key=True)
    ifname = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'interface_table'


class IosParserStaticTreeTable(models.Model):
    modelindex = models.IntegerField()
    iosmodelname = models.CharField(max_length=128)
    nodeindex = models.IntegerField()
    parentindex = models.IntegerField()
    nodename = models.CharField(max_length=128)
    nodevalue = models.CharField(max_length=128, blank=True, null=True)
    ctmattributename = models.CharField(max_length=128, blank=True, null=True)
    attributelocation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ios_parser_static_tree_table'
        unique_together = (('modelindex', 'iosmodelname', 'nodeindex'),)


class L2FrontportTable(models.Model):
    neid = models.IntegerField()
    slot_number = models.IntegerField()
    port_number = models.IntegerField()
    nni = models.NullBooleanField()
    uni = models.NullBooleanField()
    dot1q = models.NullBooleanField()
    qinq = models.NullBooleanField()
    untagged = models.NullBooleanField()
    bg_count = models.IntegerField(blank=True, null=True)
    sub_if_count = models.IntegerField(blank=True, null=True)
    port_state = models.NullBooleanField()
    pm_status = models.NullBooleanField()
    mtu_size = models.CharField(max_length=6, blank=True, null=True)
    speed = models.CharField(max_length=6, blank=True, null=True)
    duplex = models.CharField(max_length=6, blank=True, null=True)
    flowcontrol_send = models.CharField(max_length=30, blank=True, null=True)
    flowcontrol_receive = models.CharField(max_length=30, blank=True, null=True)
    cdp = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l2_frontport_table'
        unique_together = (('neid', 'slot_number', 'port_number'),)


class L2InterfaceQosclassTable(models.Model):
    neid = models.IntegerField()
    slot_number = models.IntegerField()
    bridge_group_number = models.IntegerField()
    port_number = models.IntegerField()
    port_sub_interface = models.IntegerField(blank=True, null=True)
    match_any = models.NullBooleanField()
    match_dscp = models.NullBooleanField()
    match_cos = models.NullBooleanField()
    match_ip_precedence = models.NullBooleanField()
    match_dscp_value = models.CharField(max_length=64, blank=True, null=True)
    match_cos_value = models.CharField(max_length=32, blank=True, null=True)
    match_ip_precedence_value = models.CharField(max_length=32, blank=True, null=True)
    andor = models.NullBooleanField()
    class_name = models.CharField(max_length=60, blank=True, null=True)
    cir_type = models.IntegerField(blank=True, null=True)
    max_rate_kbps = models.BigIntegerField(blank=True, null=True)
    burst_size_bps = models.BigIntegerField(blank=True, null=True)
    cir_cos_type = models.IntegerField(blank=True, null=True)
    cir_cos_value = models.IntegerField(blank=True, null=True)
    excess_action = models.IntegerField(blank=True, null=True)
    pir_burst_bps = models.BigIntegerField(blank=True, null=True)
    pir_kbps = models.BigIntegerField(blank=True, null=True)
    pir_cos_type = models.IntegerField(blank=True, null=True)
    pir_cos_value = models.IntegerField(blank=True, null=True)
    violate_action = models.IntegerField(blank=True, null=True)
    violate_cos_value = models.IntegerField(blank=True, null=True)
    beff_type = models.IntegerField(blank=True, null=True)
    beff_rate_kbps = models.BigIntegerField(blank=True, null=True)
    beff_burst_size_bps = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l2_interface_qosclass_table'


class L2InterfaceTable(models.Model):
    neid = models.ForeignKey(BridgeGroupTable, db_column='neid')
    slot_number = models.ForeignKey(BridgeGroupTable, db_column='slot_number')
    bridge_group_number = models.ForeignKey(BridgeGroupTable, db_column='bridge_group_number')
    port_number = models.IntegerField()
    port_sub_interface = models.IntegerField(blank=True, null=True)
    interface_name = models.CharField(max_length=30, blank=True, null=True)
    interface_type = models.IntegerField(blank=True, null=True)
    port_type = models.IntegerField(blank=True, null=True)
    connection_type = models.IntegerField(blank=True, null=True)
    port_state = models.IntegerField(blank=True, null=True)
    policing_type = models.IntegerField(blank=True, null=True)
    qostemplate_name = models.CharField(max_length=30, blank=True, null=True)
    mtu_size = models.CharField(max_length=30, blank=True, null=True)
    speed = models.CharField(max_length=30, blank=True, null=True)
    duplex = models.CharField(max_length=30, blank=True, null=True)
    flowcontrol_send = models.CharField(max_length=30, blank=True, null=True)
    flowcontrol_receive = models.CharField(max_length=30, blank=True, null=True)
    rstp_status = models.IntegerField(blank=True, null=True)
    cdp = models.CharField(max_length=30, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    subnet_mask = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l2_interface_table'


class L2IpslaAttributeTable(models.Model):
    source_neid = models.ForeignKey('L2IpslaTable', db_column='source_neid')
    source_phyloc = models.ForeignKey('L2IpslaTable', db_column='source_phyloc')
    ipsla_number = models.ForeignKey('L2IpslaTable', db_column='ipsla_number')
    attributename = models.CharField(max_length=50)
    attributevalue = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l2_ipsla_attribute_table'


class L2IpslaTable(models.Model):
    toponodeid = models.ForeignKey('L2VlanTable', db_column='toponodeid')
    topouniqueid = models.ForeignKey('L2VlanTable', db_column='topouniqueid')
    vlan_number = models.ForeignKey('L2VlanTable', db_column='vlan_number')
    ipsla_number = models.IntegerField()
    destination_neid = models.IntegerField(blank=True, null=True)
    destination_phyloc = models.BigIntegerField(blank=True, null=True)
    destination_addr = models.CharField(max_length=50, blank=True, null=True)
    source_neid = models.IntegerField()
    source_phyloc = models.BigIntegerField()
    source_addr = models.CharField(max_length=50, blank=True, null=True)
    operation_type = models.CharField(max_length=50, blank=True, null=True)
    operation_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l2_ipsla_table'
        unique_together = (('source_neid', 'source_phyloc', 'ipsla_number'),)


class L2VlanTable(models.Model):
    toponodeid = models.ForeignKey('L2TopologyTable', db_column='toponodeid')
    topouniqueid = models.ForeignKey('L2TopologyTable', db_column='topouniqueid')
    vlan_number = models.IntegerField()
    service_id = models.CharField(max_length=50, blank=True, null=True)
    customer_id = models.CharField(max_length=50, blank=True, null=True)
    vlanstatus = models.IntegerField(blank=True, null=True)
    managedvlan = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'l2_vlan_table'
        unique_together = (('toponodeid', 'topouniqueid', 'vlan_number'),)


class L2QostemplateQosclassTable(models.Model):
    qostemplateid = models.ForeignKey('L2QostemplateTable', db_column='qostemplateid')
    match_any = models.NullBooleanField()
    match_dscp = models.NullBooleanField()
    match_cos = models.NullBooleanField()
    match_ip_precedence = models.NullBooleanField()
    match_dscp_value = models.CharField(max_length=64, blank=True, null=True)
    match_cos_value = models.CharField(max_length=32, blank=True, null=True)
    match_ip_precedence_value = models.CharField(max_length=32, blank=True, null=True)
    andor = models.NullBooleanField()
    class_name = models.CharField(max_length=60, blank=True, null=True)
    cir_type = models.IntegerField(blank=True, null=True)
    max_rate_kbps = models.BigIntegerField(blank=True, null=True)
    burst_size_bps = models.BigIntegerField(blank=True, null=True)
    cir_cos_type = models.IntegerField(blank=True, null=True)
    cir_cos_value = models.IntegerField(blank=True, null=True)
    excess_action = models.IntegerField(blank=True, null=True)
    pir_burst_bps = models.BigIntegerField(blank=True, null=True)
    pir_kbps = models.BigIntegerField(blank=True, null=True)
    pir_cos_type = models.IntegerField(blank=True, null=True)
    pir_cos_value = models.IntegerField(blank=True, null=True)
    violate_action = models.IntegerField(blank=True, null=True)
    violate_cos_value = models.IntegerField(blank=True, null=True)
    beff_type = models.IntegerField(blank=True, null=True)
    beff_rate_kbps = models.BigIntegerField(blank=True, null=True)
    beff_burst_size_bps = models.BigIntegerField(blank=True, null=True)
    classorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'l2qostemplate_qosclass_table'


class L2QostemplateTable(models.Model):
    qostemplateid = models.IntegerField(primary_key=True)
    qostemplatename = models.CharField(max_length=50)
    qostemplatetype = models.IntegerField(blank=True, null=True)
    qostemplatedescription = models.CharField(max_length=257, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l2qostemplate_table'


class L2TopologyCircuitsTable(models.Model):
    toponodeid = models.ForeignKey('L2TopologyTable', db_column='toponodeid')
    topouniqueid = models.ForeignKey('L2TopologyTable', db_column='topouniqueid')
    nodeid = models.IntegerField()
    uniqueid = models.IntegerField()
    linkid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'l2topology_circuits_table'


class L2TopologyTable(models.Model):
    toponodeid = models.IntegerField()
    topouniqueid = models.IntegerField()
    topotype = models.IntegerField(blank=True, null=True)
    topology_name = models.CharField(max_length=50, blank=True, null=True)
    topodescription = models.CharField(max_length=256, blank=True, null=True)
    alarmseverity = models.IntegerField(blank=True, null=True)
    topostatus = models.IntegerField(blank=True, null=True)
    toposize = models.IntegerField(blank=True, null=True)
    topoprotection = models.IntegerField(blank=True, null=True)
    toporesyncstatus = models.IntegerField(blank=True, null=True)
    topooperstatus = models.IntegerField(blank=True, null=True)
    bw_sp_management = models.IntegerField(blank=True, null=True)
    bw_committed = models.IntegerField(blank=True, null=True)
    bw_best_effort = models.IntegerField(blank=True, null=True)
    topoconstate = models.IntegerField(blank=True, null=True)
    cos_commit = models.IntegerField(blank=True, null=True)
    bw_utilized = models.BigIntegerField(blank=True, null=True)
    bw_available = models.BigIntegerField(blank=True, null=True)
    bw_avvid_control = models.IntegerField(blank=True, null=True)
    cos_sp_management = models.CharField(max_length=128, blank=True, null=True)
    cos_committed = models.CharField(max_length=128, blank=True, null=True)
    cos_avvid_voicevideo = models.CharField(max_length=128, blank=True, null=True)
    cos_avvid_control = models.CharField(max_length=128, blank=True, null=True)
    bw_group1 = models.IntegerField(blank=True, null=True)
    bw_group2 = models.IntegerField(blank=True, null=True)
    cos_group1 = models.CharField(max_length=128, blank=True, null=True)
    cos_group2 = models.CharField(max_length=128, blank=True, null=True)
    topoaliasname = models.CharField(max_length=64, blank=True, null=True)
    bw_a0 = models.IntegerField(blank=True, null=True)
    bw_a1 = models.IntegerField(blank=True, null=True)
    bw_b_cir = models.IntegerField(blank=True, null=True)
    class_sp_mgmt = models.CharField(max_length=128, blank=True, null=True)
    class_cir = models.CharField(max_length=128, blank=True, null=True)
    class_best_effort = models.CharField(max_length=128, blank=True, null=True)
    class_avvid_ctrl = models.CharField(max_length=128, blank=True, null=True)
    class_avvid_voicevideo = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l2topology_table'
        unique_together = (('toponodeid', 'topouniqueid'),)


class LayerInstance(models.Model):
    rate = models.CharField(max_length=765)
    tp = models.ForeignKey('TerminationPointTable')

    class Meta:
        managed = False
        db_table = 'layer_instance'
        unique_together = (('tp_id', 'rate'),)


class LayerInstanceParameters(models.Model):
    layerinstanceentity_tp = models.ForeignKey(LayerInstance)
    layerinstanceentity_rate = models.ForeignKey(LayerInstance, db_column='layerinstanceentity_rate')
    parameters = models.CharField(max_length=765, blank=True, null=True)
    parameters_key = models.CharField(max_length=765)

    class Meta:
        managed = False
        db_table = 'layer_instance_parameters'
        unique_together = (('layerinstanceentity_tp_id', 'layerinstanceentity_rate', 'parameters_key'),)


class LinkCapacityRule(models.Model):
    dtype = models.CharField(max_length=31)
    linkid = models.IntegerField(primary_key=True)
    capacityvalue = models.IntegerField(blank=True, null=True)
    capacitymeasure = models.CharField(max_length=80)
    description = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_capacity_rule'


class LinkCapacityTable(models.Model):
    linkid = models.IntegerField()
    linkcapacitypercentage = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'link_capacity_table'


class LinkForAlarmTable(models.Model):
    nedbid = models.IntegerField()
    physicalloc = models.BigIntegerField()
    linkid = models.ForeignKey('LinkTable', db_column='linkid')
    tp_role = models.CharField(max_length=765, blank=True, null=True)
    tp_key = models.CharField(max_length=765, blank=True, null=True)
    side = models.IntegerField(blank=True, null=True)
    link_key = models.CharField(max_length=765, blank=True, null=True)
    link_layer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_for_alarm_table'
        unique_together = (('nedbid', 'physicalloc', 'linkid'),)


class LinkLayerMappingTable(models.Model):
    linklayerid = models.IntegerField(primary_key=True)
    linklayerstring = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_layer_mapping_table'


class LinkTable(models.Model):
    linkid = models.IntegerField(primary_key=True)
    linksrcnode = models.ForeignKey('NeInfoTable', db_column='linksrcnode')
    linksrcmoduletype = models.IntegerField()
    linksrcphysicalloc = models.BigIntegerField()
    linksrcmodeltype = models.IntegerField()
    linksrcifindex = models.BigIntegerField()
    linksrcobjecttype = models.IntegerField(blank=True, null=True)
    linkdstnode = models.ForeignKey('NeInfoTable', db_column='linkdstnode')
    linkdstmoduletype = models.IntegerField()
    linkdstphysicalloc = models.BigIntegerField()
    linkdstmodeltype = models.IntegerField()
    linkdstifindex = models.BigIntegerField()
    linkdstobjecttype = models.IntegerField(blank=True, null=True)
    linklayer = models.ForeignKey(LinkLayerMappingTable, db_column='linklayer')
    linksize = models.IntegerField()
    linkvalid = models.BooleanField()
    legindex = models.NullBooleanField()
    cablegroupid = models.IntegerField(blank=True, null=True)
    linkprovtype = models.BooleanField()
    linkconnectiontype = models.BooleanField()
    linktype = models.IntegerField()
    linkprottype = models.IntegerField()
    linkprotrole = models.BooleanField()
    linkdirection = models.BooleanField()
    linkstate = models.BooleanField()
    useforrouting = models.BooleanField()
    linkname = models.CharField(max_length=256)
    linkdescription = models.CharField(max_length=256, blank=True, null=True)
    numcriticalalarms = models.IntegerField(blank=True, null=True)
    nummajoralarms = models.IntegerField(blank=True, null=True)
    numminoralarms = models.IntegerField(blank=True, null=True)
    numwarningalarms = models.IntegerField(blank=True, null=True)
    linksrcphylocunmanaged = models.CharField(max_length=300, blank=True, null=True)
    linkdestphylocunmanaged = models.CharField(max_length=300, blank=True, null=True)
    linkunmanaged = models.NullBooleanField()
    linkcost = models.IntegerField(blank=True, null=True)
    linksrlglist = models.CharField(max_length=256, blank=True, null=True)
    stsize = models.IntegerField(blank=True, null=True)
    sttype = models.IntegerField(blank=True, null=True)
    stcount = models.IntegerField(blank=True, null=True)
    stnodeid = models.IntegerField(blank=True, null=True)
    stuniqueid = models.IntegerField(blank=True, null=True)
    linkaliasname = models.CharField(max_length=256, blank=True, null=True)
    linkblsrringid = models.CharField(max_length=8, blank=True, null=True)
    linksrcctcindex = models.IntegerField(blank=True, null=True)
    linkdstctcindex = models.IntegerField(blank=True, null=True)
    cktnodeid = models.IntegerField(blank=True, null=True)
    cktuniqueid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_table'
        unique_together = (('linkname', 'legindex'),)


class LinkidToUniqueid(models.Model):
    linkid = models.IntegerField()
    uniqueid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'linkid_to_uniqueid'
        unique_together = (('linkid', 'uniqueid'),)


class LoggerConfig(models.Model):
    serviceid = models.IntegerField()
    modulename = models.CharField(max_length=50)
    log_level = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logger_config'
        unique_together = (('serviceid', 'modulename'),)


class ManagedEtTab(models.Model):
    mng_entity_type = models.IntegerField()
    mng_entity_id_num = models.IntegerField()
    mng_entity_id2_num = models.IntegerField()
    nedbaccessid = models.ForeignKey('NeInfoTable', db_column='nedbaccessid')
    field1_num = models.IntegerField()
    field2_num = models.BigIntegerField()
    field3_num = models.BigIntegerField()
    field4_num = models.IntegerField()
    customer_id_str = models.CharField(max_length=256, blank=True, null=True)
    service_id_str = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managed_et_tab'
        unique_together = (('mng_entity_type', 'mng_entity_id_num', 'mng_entity_id2_num', 'nedbaccessid', 'field1_num', 'field2_num', 'field3_num'),)


class MapBackgroundFileTable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filecontent = models.BinaryField(blank=True, null=True)
    filename = models.CharField(max_length=765, blank=True, null=True)
    filesize = models.BigIntegerField()
    type = models.CharField(max_length=765, blank=True, null=True)
    background = models.ForeignKey('MapBackgroundTable', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_background_file_table'


class MapBackgroundTable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    addedat = models.DateTimeField(blank=True, null=True)
    addedby = models.CharField(max_length=765, blank=True, null=True)
    description = models.CharField(max_length=765, blank=True, null=True)
    name = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_background_table'


class MapBadgeConfTable(models.Model):
    config = models.ForeignKey('MapElementConfTable')
    visible_on_group = models.NullBooleanField()
    position = models.CharField(max_length=765, blank=True, null=True)
    type = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_badge_conf_table'


class MapCoordinateTable(models.Model):
    coordindex = models.BigIntegerField(primary_key=True)
    parentnodetype = models.NullBooleanField()
    parentnodeid = models.IntegerField(blank=True, null=True)
    childnodetype = models.NullBooleanField()
    childnodeid = models.IntegerField(blank=True, null=True)
    coordx = models.IntegerField(blank=True, null=True)
    coordy = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_coordinate_table'


class MapCustTable(models.Model):
    customizationid = models.IntegerField(primary_key=True)
    mapcoordx = models.IntegerField(blank=True, null=True)
    mapcoordy = models.IntegerField(blank=True, null=True)
    iconimageid = models.IntegerField(blank=True, null=True)
    bgiconimageid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    grouporneid = models.IntegerField(blank=True, null=True)
    treenodetype = models.NullBooleanField()
    zoomfactor = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    viewpositionx = models.IntegerField(blank=True, null=True)
    viewpositiony = models.IntegerField(blank=True, null=True)
    showlayermode = models.NullBooleanField()
    maplayerrate = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_cust_table'


class MapCustom(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    bg = models.ForeignKey(MapBackgroundTable, db_column='bg', blank=True, null=True)
    mapid = models.ForeignKey('TopologyMap', db_column='mapid', blank=True, null=True)
    type = models.CharField(max_length=765, blank=True, null=True)
    userid = models.ForeignKey('UserTable', db_column='userid', blank=True, null=True)
    viewpositionx = models.IntegerField(blank=True, null=True)
    viewpositiony = models.IntegerField(blank=True, null=True)
    zoomfactor = models.FloatField(blank=True, null=True)
    iconsthreshold = models.FloatField(blank=True, null=True)
    defaultbackground = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'map_custom'


class MapElementConfTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bundlewidth = models.IntegerField()
    collapsedasdefault = models.BooleanField()
    distancebetweenlinks = models.IntegerField()
    highlighticononalarm = models.BooleanField()
    linkwidth = models.IntegerField()
    minlinksforabundle = models.IntegerField()
    linkside = models.NullBooleanField()
    linkdirection = models.NullBooleanField()
    linkrefreshtimeout = models.IntegerField(blank=True, null=True)
    ottlink = models.NullBooleanField()
    omslink = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'map_element_conf_table'


class MapImageTable(models.Model):
    mapimageid = models.IntegerField(primary_key=True)
    imagename = models.CharField(max_length=256, blank=True, null=True)
    imagefile = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_image_table'


class MapLabelConfTable(models.Model):
    config = models.ForeignKey(MapElementConfTable)
    type = models.CharField(max_length=765, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'map_label_conf_table'
        unique_together = (('config_id', 'position'),)


class MapLinkTable(models.Model):
    maplinkid = models.IntegerField(unique=True)
    node1type = models.BooleanField()
    node1id = models.IntegerField()
    node2type = models.BooleanField()
    node2id = models.IntegerField()
    linkcolor = models.IntegerField(blank=True, null=True)
    linkwidth = models.IntegerField(blank=True, null=True)
    linkname = models.CharField(max_length=32, blank=True, null=True)
    linkdescription = models.CharField(max_length=64, blank=True, null=True)
    linktooltip = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_link_table'
        unique_together = (('node1type', 'node1id', 'node2type', 'node2id'),)


class MapPosition(models.Model):
    positionid = models.IntegerField(primary_key=True)
    positionx = models.IntegerField(blank=True, null=True)
    positiony = models.IntegerField(blank=True, null=True)
    customizationid = models.ForeignKey(MapCustom, db_column='customizationid', blank=True, null=True)
    nodeid = models.IntegerField(blank=True, null=True)
    nodepositiontype = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_position'


class MatrixFlowDomainTable(models.Model):
    mfd_ne_db = models.ForeignKey('NeInfoTable')
    fd_name = models.ForeignKey(FlowDomainTable, db_column='fd_name', blank=True, null=True)
    mfd_user_label = models.CharField(max_length=64, blank=True, null=True)
    mfd_native_name = models.CharField(max_length=64)
    mfd_owner = models.CharField(max_length=64, blank=True, null=True)
    mfd_transm_params = models.CharField(max_length=512, blank=True, null=True)
    mfd_net_access_domain = models.CharField(max_length=64, blank=True, null=True)
    mfd_flexible = models.NullBooleanField()
    mfd_additional_info = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matrix_flow_domain_table'
        unique_together = (('mfd_ne_db_id', 'mfd_native_name'),)


class McardTable(models.Model):
    nedbaccessid = models.IntegerField()
    slotnumber = models.IntegerField(blank=True, null=True)
    configstate = models.IntegerField(blank=True, null=True)
    additionalinfo = models.CharField(max_length=256, blank=True, null=True)
    protectcardnedbid = models.IntegerField(blank=True, null=True)
    protectcardslotnumber = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mcard_table'


class Mib2InterfaceTable(models.Model):
    ifdbaccessid = models.IntegerField(primary_key=True)
    nedbaccessid = models.ForeignKey('NeInfoTable', db_column='nedbaccessid')
    physicalloc = models.BigIntegerField()
    moduletype = models.IntegerField(blank=True, null=True)
    neifindex = models.BigIntegerField()
    objecttype = models.IntegerField()
    modeltype = models.IntegerField()
    phyifindex = models.IntegerField(blank=True, null=True)
    ifindex = models.IntegerField()
    iftype = models.IntegerField()
    ifexttype = models.IntegerField(blank=True, null=True)
    ifspecifictype = models.IntegerField(blank=True, null=True)
    ifdescr = models.CharField(max_length=255)
    ifname = models.CharField(max_length=50)
    ifspeed = models.CharField(max_length=15, blank=True, null=True)
    ifadminstatus = models.IntegerField()
    ifoperstatus = models.IntegerField()
    ifhighspeed = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mib2_interface_table'


class MlsQosPmapTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mls_qos_pmap_table'


class ModelIndexTable(models.Model):
    modelindex = models.IntegerField()
    modeltype = models.IntegerField()
    name = models.CharField(max_length=128, blank=True, null=True)
    issupported = models.NullBooleanField()
    propertysheetset = models.IntegerField(blank=True, null=True)
    schema = models.CharField(max_length=255, blank=True, null=True)
    statictreeset = models.IntegerField(blank=True, null=True)
    tagset = models.CharField(max_length=128, blank=True, null=True)
    train = models.CharField(max_length=50, blank=True, null=True)
    hierarchyorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_index_table'
        unique_together = (('modelindex', 'modeltype'),)


class ModelTypeTable(models.Model):
    modeltype = models.IntegerField(primary_key=True)
    modeltypename = models.CharField(max_length=64)
    modelsortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_type_table'


class Module155XxCommunityString(models.Model):
    target = models.CharField(primary_key=True, max_length=64)
    readstring = models.CharField(max_length=64, blank=True, null=True)
    retry = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    writestring = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'module155xx_community_string'


class Module155XxVtoidTable(models.Model):
    moduletype = models.IntegerField(primary_key=True)
    vendoroid = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'module155xx_vtoid_table'


class ModuleTypeMllInfo(models.Model):
    moduletype = models.IntegerField()
    layerrate = models.IntegerField()
    modeltype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'module_type_mll_info'
        unique_together = (('moduletype', 'layerrate', 'modeltype'),)


class ModuleTypeTable(models.Model):
    moduletype = models.IntegerField()
    modulename = models.CharField(max_length=64, blank=True, null=True)
    modeltype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'module_type_table'
        unique_together = (('moduletype', 'modeltype'),)


class MplsDataServiceTable(models.Model):
    nedbid = models.ForeignKey('MplsServiceTable', db_column='nedbid')
    ptsindex = models.ForeignKey('MplsServiceTable', db_column='ptsindex')
    serviceid = models.ForeignKey('MplsServiceTable', db_column='serviceid')
    servicedata = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'mpls_data_service_table'


class MplsLspCtp(models.Model):
    nedbid = models.ForeignKey('MplsServiceTable', db_column='nedbid')
    ptsindex = models.ForeignKey('MplsServiceTable', db_column='ptsindex')
    serviceid = models.ForeignKey('MplsServiceTable', db_column='serviceid')
    workprot = models.IntegerField()
    ctcindex = models.IntegerField()
    phyloc = models.BigIntegerField()
    lspnum = models.IntegerField()
    linknum = models.IntegerField()
    locallabel = models.IntegerField()
    outlabel = models.IntegerField()
    ctmuniqid = models.IntegerField()
    linkid = models.IntegerField()
    ctptype = models.BooleanField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    islockout = models.BooleanField()
    isactive = models.BooleanField()
    lsppathdefdirection = models.BooleanField()
    slotmoduletype = models.IntegerField()
    portmoduletype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mpls_lsp_ctp'
        unique_together = (('nedbid', 'ptsindex', 'serviceid', 'ctcindex'),)


class MplsLspXc(models.Model):
    nedbid = models.ForeignKey('MplsServiceTable', db_column='nedbid')
    ptsindex = models.ForeignKey('MplsServiceTable', db_column='ptsindex')
    serviceid = models.ForeignKey('MplsServiceTable', db_column='serviceid')
    wfwdctcindex = models.IntegerField()
    wrevctcindex = models.IntegerField()
    pfwdctcindex = models.IntegerField()
    prevctcindex = models.IntegerField()
    wlspnum = models.IntegerField()
    plspnum = models.IntegerField()
    xctype = models.BooleanField()
    servicename = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_lsp_xc'
        unique_together = (('nedbid', 'ptsindex', 'serviceid'),)


class MplsNeTable(models.Model):
    nedbid = models.ForeignKey('NeInfoTable', db_column='nedbid')
    ptsindex = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mpls_ne_table'
        unique_together = (('nedbid', 'ptsindex'),)


class MplsQosActionTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765)
    cirvalue = models.FloatField(blank=True, null=True)
    cirunit = models.IntegerField(blank=True, null=True)
    pirvalue = models.FloatField(blank=True, null=True)
    pirunit = models.IntegerField(blank=True, null=True)
    peakburstsizevalue = models.FloatField(blank=True, null=True)
    peakburstsizeunit = models.IntegerField(blank=True, null=True)
    burstsizevalue = models.FloatField(blank=True, null=True)
    burstsizeunit = models.IntegerField(blank=True, null=True)
    averageratevalue = models.FloatField(blank=True, null=True)
    averagerateunit = models.IntegerField(blank=True, null=True)
    priorityvalue = models.FloatField(blank=True, null=True)
    priorityunit = models.IntegerField(blank=True, null=True)
    blankpriority = models.NullBooleanField()
    minimumbandwidthvalue = models.FloatField(blank=True, null=True)
    minimumbandwidthunit = models.IntegerField(blank=True, null=True)
    remainingbandwidthvalue = models.FloatField(blank=True, null=True)
    remainingbandwidthunit = models.IntegerField(blank=True, null=True)
    ratecode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_qos_action_table'


class MplsQosAmTable(models.Model):
    id = models.ForeignKey(MplsQosActionTable, db_column='id')
    attributenamecode = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_qos_am_table'


class MplsQosClassMapTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765)
    vlan = models.CharField(max_length=765, blank=True, null=True)
    cos = models.CharField(max_length=765, blank=True, null=True)
    precedence = models.CharField(max_length=765, blank=True, null=True)
    dscp = models.CharField(max_length=765, blank=True, null=True)
    mplsexperimental = models.CharField(max_length=765, blank=True, null=True)
    qosgroup = models.CharField(max_length=765, blank=True, null=True)
    matchall = models.NullBooleanField()
    defaultclassmap = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mpls_qos_class_map_table'


class MplsQosConformPaTable(models.Model):
    id = models.ForeignKey(MplsQosActionTable, db_column='id')
    namecode = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_qos_conform_pa_table'


class MplsQosExceedPaTable(models.Model):
    id = models.ForeignKey(MplsQosActionTable, db_column='id')
    namecode = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_qos_exceed_pa_table'


class MplsQosMapperTable(models.Model):
    id = models.ForeignKey('MplsQosTablemapTable', db_column='id')
    qosgroup = models.IntegerField(blank=True, null=True)
    discardclass = models.IntegerField(blank=True, null=True)
    mplsorcos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_qos_mapper_table'


class MplsQosPolicyTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    classmap = models.ForeignKey(MplsQosClassMapTable, db_column='classmap', blank=True, null=True)
    action = models.ForeignKey(MplsQosActionTable, db_column='action', blank=True, null=True)
    childpolicy = models.ForeignKey(MlsQosPmapTable, db_column='childpolicy', blank=True, null=True)
    policymapid = models.ForeignKey(MlsQosPmapTable, db_column='policymapid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_qos_policy_table'


class MplsQosTablemapTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765)
    defaultcopy = models.NullBooleanField()
    defaultvalue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_qos_tablemap_table'


class MplsQosViolatePaTable(models.Model):
    id = models.ForeignKey(MplsQosActionTable, db_column='id')
    namecode = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpls_qos_violate_pa_table'


class MplsServiceTable(models.Model):
    nedbid = models.ForeignKey(MplsNeTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsNeTable, db_column='ptsindex')
    serviceid = models.IntegerField()
    servicetype = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    servicedescription = models.CharField(max_length=256, blank=True, null=True)
    lasttime = models.BigIntegerField()
    adminstate = models.IntegerField()
    operstate = models.IntegerField()
    markbad = models.BooleanField()
    xctype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mpls_service_table'
        unique_together = (('nedbid', 'ptsindex', 'serviceid'),)


class MplsTpEp(models.Model):
    nedbid = models.ForeignKey(MplsServiceTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsServiceTable, db_column='ptsindex')
    serviceid = models.ForeignKey(MplsServiceTable, db_column='serviceid')
    ctcindex = models.IntegerField()
    phyloc = models.BigIntegerField()
    bdfname = models.CharField(max_length=256, blank=True, null=True)
    srctunnelnum = models.IntegerField()
    dsttunnelnum = models.IntegerField()
    ctmworkinguniqid = models.IntegerField()
    ctmprotecteduniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    txbandwidth = models.BigIntegerField()
    rxbandwidth = models.BigIntegerField()
    operstate = models.BooleanField()
    adminstate = models.BooleanField()
    ctmuniqid = models.IntegerField()
    isprotected = models.BooleanField()
    srcnodeip = models.CharField(max_length=256, blank=True, null=True)
    dstnodeip = models.CharField(max_length=256, blank=True, null=True)
    wlspnum = models.IntegerField()
    plspnum = models.IntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)
    slotmoduletype = models.IntegerField()
    portmoduletype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mpls_tp_ep'
        unique_together = (('nedbid', 'ptsindex', 'serviceid'),)


class NeAuditTrailTable(models.Model):
    nedbaccessid = models.IntegerField()
    sequencenumber = models.IntegerField()
    timestamp = models.DateField()
    operationdescription = models.CharField(max_length=256)
    operationstatus = models.CharField(max_length=1, blank=True, null=True)
    neuserid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_audit_trail_table'
        unique_together = (('nedbaccessid', 'sequencenumber', 'timestamp', 'operationdescription'),)


class NeInfoTable(models.Model):
    nedbaccessid = models.IntegerField(primary_key=True)
    nesysid = models.CharField(unique=True, max_length=128)
    neipaddr = models.IntegerField(blank=True, null=True)
    nensapaddr = models.CharField(unique=True, max_length=60, blank=True, null=True)
    nestate = models.BooleanField()
    isneconnected = models.BooleanField()
    gneid = models.IntegerField(blank=True, null=True)
    nedescription = models.CharField(max_length=256, blank=True, null=True)
    neconfigmode = models.IntegerField(blank=True, null=True)
    nesnmpcommstring = models.CharField(max_length=256, blank=True, null=True)
    necllicode = models.CharField(max_length=64, blank=True, null=True)
    nestatechangetime = models.DateField(blank=True, null=True)
    nemodeltype = models.IntegerField(blank=True, null=True)
    nemodelindex = models.IntegerField(blank=True, null=True)
    nemodelstatus = models.IntegerField(blank=True, null=True)
    nesubnetworkid = models.IntegerField(blank=True, null=True)
    netimeoffset = models.IntegerField(blank=True, null=True)
    neledstatus = models.TextField(blank=True, null=True)  # This field type is a guess.
    nesystemtitle = models.CharField(max_length=64, blank=True, null=True)
    neuserlabel = models.CharField(max_length=64, blank=True, null=True)
    nevendorname = models.CharField(max_length=32, blank=True, null=True)
    neversion = models.CharField(max_length=128, blank=True, null=True)
    nenumactivecriticalerrors = models.IntegerField(blank=True, null=True)
    nenumactivemajorerrors = models.IntegerField(blank=True, null=True)
    nenumactiveminorerrors = models.IntegerField(blank=True, null=True)
    nepmenabled = models.NullBooleanField()
    nenodeid = models.IntegerField(blank=True, null=True)
    neinventorylastchanged = models.BigIntegerField(blank=True, null=True)
    nesubnetmask = models.IntegerField(blank=True, null=True)
    nedefaultgateway = models.IntegerField(blank=True, null=True)
    nenumunactivecriticalerrors = models.IntegerField(blank=True, null=True)
    nenumunactivemajorerrors = models.IntegerField(blank=True, null=True)
    nenumunactiveminorerrors = models.IntegerField(blank=True, null=True)
    nenumcleared = models.IntegerField(blank=True, null=True)
    displaymodelname = models.CharField(max_length=15, blank=True, null=True)
    gwtl1username = models.CharField(max_length=20, blank=True, null=True)
    gwtl1passwd = models.CharField(max_length=20, blank=True, null=True)
    serviceid = models.BigIntegerField(blank=True, null=True)
    deletestate = models.NullBooleanField()
    configsyncstatus = models.NullBooleanField()
    neusername = models.CharField(max_length=64, blank=True, null=True)
    neuserpassword = models.CharField(max_length=64, blank=True, null=True)
    nediscoverystate = models.BooleanField()
    nerobustpmenabled = models.NullBooleanField()
    securityticket = models.CharField(max_length=32, blank=True, null=True)
    robustpmenabletime = models.DateField(blank=True, null=True)
    debuglevel = models.NullBooleanField()
    robust1daypmenabletime = models.DateField(blank=True, null=True)
    secondsbehindutc = models.BigIntegerField(blank=True, null=True)
    secondsdstbehindutc = models.BigIntegerField(blank=True, null=True)
    nesngrpid = models.IntegerField(blank=True, null=True)
    nealiasid = models.CharField(max_length=128)
    ismultishelf = models.NullBooleanField()
    roletype = models.CharField(max_length=30, blank=True, null=True)
    nevirtualipaddr = models.IntegerField(blank=True, null=True)
    istunnelrequired = models.NullBooleanField()
    neipv6addr = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_ipv6 = models.NullBooleanField()
    preprovisioned_ip = models.NullBooleanField()
    isdss = models.NullBooleanField()
    ne_snmp_auth_prot = models.CharField(max_length=10, blank=True, null=True)
    ne_snmp_auth_pwd = models.CharField(max_length=32, blank=True, null=True)
    ne_snmp_eid = models.CharField(max_length=64, blank=True, null=True)
    ne_snmp_priv_pwd = models.CharField(max_length=32, blank=True, null=True)
    ne_snmp_uname = models.CharField(max_length=20, blank=True, null=True)
    ne_snmp_version = models.NullBooleanField()
    neinventorytimestamp = models.DateField(blank=True, null=True)
    gneid_nullable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_info_table'


class NeInventoryTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduleindex = models.IntegerField()
    modulename = models.CharField(max_length=32, blank=True, null=True)
    modulepartnum = models.CharField(max_length=32, blank=True, null=True)
    modulecleicode = models.CharField(max_length=32, blank=True, null=True)
    modulehwversion = models.CharField(max_length=32, blank=True, null=True)
    moduleswversion = models.CharField(max_length=32, blank=True, null=True)
    moduleserialnumber = models.CharField(max_length=32, blank=True, null=True)
    moduledateofmanuf = models.DateField(blank=True, null=True)
    moduledateofentry = models.DateField(blank=True, null=True)
    modulehoursinuse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_inventory_table'
        unique_together = (('nedbaccessid', 'moduleindex'),)


class NeModelState(models.Model):
    node_id = models.BigIntegerField()
    model_type = models.BigIntegerField()
    model_index = models.BigIntegerField()
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_model_state'
        unique_together = (('node_id', 'model_type', 'model_index'),)


class NeModelType(models.Model):
    node_id = models.BigIntegerField()
    model_type = models.BigIntegerField()
    signature = models.BinaryField(blank=True, null=True)
    sequence_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_model_type'
        unique_together = (('node_id', 'model_type'),)


class NePortStatusTable(models.Model):
    nedbaccessid = models.IntegerField()
    portindex = models.IntegerField()
    portoperstate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ne_port_status_table'


class NePurgedDbgTable(models.Model):
    nedbaccessid = models.IntegerField()
    nesysid = models.CharField(max_length=128)
    num_rows = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_purged_dbg_table'


class NePurgingSlowTables(models.Model):
    nedbaccessid = models.IntegerField()
    nesysid = models.CharField(max_length=128)
    ne_type = models.CharField(max_length=3)
    tablename = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'ne_purging_slow_tables'


class NeSnmpv3GroupsTable(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    group_name = models.CharField(max_length=32)
    security_level = models.CharField(max_length=30)
    read_view_access = models.CharField(max_length=32, blank=True, null=True)
    write_view_access = models.CharField(max_length=32, blank=True, null=True)
    notify_view_access = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_snmpv3_groups_table'
        unique_together = (('nedbaccessid', 'group_name', 'security_level'),)


class NeSnmpv3NfilterTable(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    filter_profile_name = models.CharField(max_length=32)
    subtreeoid = models.CharField(max_length=200)
    bit_mask = models.CharField(max_length=32, blank=True, null=True)
    filter_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_snmpv3_nfilter_table'
        unique_together = (('nedbaccessid', 'filter_profile_name', 'subtreeoid'),)


class NeSnmpv3ProxyFwdTable(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    row_id = models.CharField(max_length=32)
    context_engine_id = models.CharField(max_length=32, blank=True, null=True)
    target_ip = models.CharField(max_length=50, blank=True, null=True)
    local_user = models.CharField(max_length=32, blank=True, null=True)
    remote_user = models.CharField(max_length=32, blank=True, null=True)
    proxy_type = models.CharField(max_length=5, blank=True, null=True)
    security_level = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_snmpv3_proxy_fwd_table'
        unique_together = (('nedbaccessid', 'row_id'),)


class NeSnmpv3ProxyTrapFwdTable(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    row_id = models.CharField(max_length=40)
    context_engine_id = models.CharField(max_length=32, blank=True, null=True)
    tag = models.CharField(max_length=32, blank=True, null=True)
    incoming_user = models.CharField(max_length=32, blank=True, null=True)
    security_level = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_snmpv3_proxy_trap_fwd_table'
        unique_together = (('nedbaccessid', 'row_id'),)


class NeSnmpv3TrapDestTable(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    target_address = models.CharField(max_length=50)
    udp_port = models.CharField(max_length=10)
    user_name = models.CharField(max_length=32)
    security_level = models.CharField(max_length=30)
    filter_profile_name = models.CharField(max_length=32, blank=True, null=True)
    proxy_traps_only = models.CharField(max_length=6, blank=True, null=True)
    proxy_tag = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_snmpv3_trap_dest_table'
        unique_together = (('nedbaccessid', 'target_address', 'udp_port', 'user_name', 'security_level'),)


class NeSnmpv3UsersTable(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    user_name = models.CharField(max_length=32)
    group_name = models.CharField(max_length=32, blank=True, null=True)
    authentication_protocol = models.CharField(max_length=6, blank=True, null=True)
    privacy_protocol = models.CharField(max_length=6, blank=True, null=True)
    engine_id = models.CharField(max_length=40)
    engine_id_len = models.CharField(max_length=4, blank=True, null=True)
    boots = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_snmpv3_users_table'
        unique_together = (('nedbaccessid', 'user_name', 'engine_id'),)


class NeSnmpv3ViewsTable(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    view_name = models.CharField(max_length=32)
    subtreeoid = models.CharField(max_length=200)
    mask = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_snmpv3_views_table'
        unique_together = (('nedbaccessid', 'view_name', 'subtreeoid'),)


class NeSwimageTable(models.Model):
    nedbaccessid = models.IntegerField(primary_key=True)
    activeimagename = models.CharField(max_length=64, blank=True, null=True)
    standbyimagename = models.CharField(max_length=64, blank=True, null=True)
    defaultimagename = models.CharField(max_length=64, blank=True, null=True)
    inprogress = models.NullBooleanField()
    physicalloc = models.BigIntegerField(blank=True, null=True)
    partialupgrade = models.NullBooleanField()
    type = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ne_swimage_table'


class NeidTemp(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    neid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neid_temp'


class Netmanagedobject(models.Model):
    id = models.BigIntegerField(primary_key=True)
    modelname = models.CharField(unique=True, max_length=765, blank=True, null=True)
    netid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'netmanagedobject'


class NetworkPartitionTable(models.Model):
    npid = models.IntegerField(primary_key=True)
    npname = models.CharField(unique=True, max_length=128)
    npdescription = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'network_partition_table'


class NgxpBetGtsTable(models.Model):
    nedbid = models.ForeignKey(MplsNeTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsNeTable, db_column='ptsindex')
    gts = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ngxp_bet_gts_table'
        unique_together = (('nedbid', 'ptsindex'),)


class NgxpBetTable(models.Model):
    nedbid = models.ForeignKey(MplsNeTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsNeTable, db_column='ptsindex')
    rangeid = models.IntegerField()
    cts = models.BigIntegerField()
    dts = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ngxp_bet_table'
        unique_together = (('nedbid', 'ptsindex', 'rangeid'),)


class NgxpSidUpdateTable(models.Model):
    nedbid = models.ForeignKey(MplsNeTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsNeTable, db_column='ptsindex')
    sid = models.IntegerField()
    type = models.IntegerField()
    tou = models.IntegerField()
    uuid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ngxp_sid_update_table'


class ObjectAttrMappingTable(models.Model):
    attrindex = models.ForeignKey('Objectattributetable', db_column='attrindex')
    attrtype = models.IntegerField()
    featureid = models.CharField(max_length=32, blank=True, null=True)
    supportedlayerrates = models.CharField(max_length=64)
    supportedmoduletype = models.CharField(max_length=64)
    metadataindex = models.ForeignKey('Objectattributetable', db_column='metadataindex')
    location = models.IntegerField()
    direction = models.IntegerField()
    granularity = models.IntegerField()
    counterid = models.CharField(max_length=33)
    tmf_name = models.CharField(max_length=33)
    tmf_thtype = models.IntegerField()
    thtype = models.IntegerField()
    counttype = models.IntegerField()
    pmviewname = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'object_attr_mapping_table'


class ObjectRelationshipTable(models.Model):
    modeltype = models.IntegerField()
    relationshiptype = models.BooleanField()
    selfobjectindex = models.IntegerField()
    relatedobjectindex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'object_relationship_table'
        unique_together = (('modeltype', 'selfobjectindex', 'relatedobjectindex'),)


class ObjectThMappingTable(models.Model):
    th_id = models.IntegerField(blank=True, null=True)
    th_name = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object_th_mapping_table'


class Objectattributetable(models.Model):
    metadataindex = models.IntegerField()
    attrindex = models.IntegerField()
    parentindex = models.IntegerField(blank=True, null=True)
    colid = models.IntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    displaytext = models.CharField(max_length=256, blank=True, null=True)
    attrclass = models.IntegerField(blank=True, null=True)
    attrtype = models.IntegerField(blank=True, null=True)
    expbase = models.IntegerField(blank=True, null=True)
    exponent = models.IntegerField(blank=True, null=True)
    factorydefault = models.CharField(max_length=32, blank=True, null=True)
    customerdefault = models.CharField(max_length=32, blank=True, null=True)
    minval = models.CharField(max_length=32, blank=True, null=True)
    maxval = models.CharField(max_length=32, blank=True, null=True)
    enumval = models.CharField(max_length=4000, blank=True, null=True)
    incrval = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    unit = models.CharField(max_length=60, blank=True, null=True)
    attraccess = models.IntegerField(blank=True, null=True)
    mandatory = models.NullBooleanField()
    attrgroup = models.IntegerField(blank=True, null=True)
    maxlen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objectattributetable'
        unique_together = (('metadataindex', 'attrindex'),)


class Objecttypetable(models.Model):
    modeltype = models.IntegerField()
    objectindex = models.IntegerField()
    metadataindex = models.IntegerField(blank=True, null=True)
    objshortname = models.CharField(max_length=32)
    objlongname = models.CharField(max_length=128, blank=True, null=True)
    parentindex = models.IntegerField(blank=True, null=True)
    boardname = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objecttypetable'


class OmsCircuitSpanTable(models.Model):
    omsspanid = models.IntegerField()
    omslinkid = models.ForeignKey(LinkTable, db_column='omslinkid')
    otslinkid = models.ForeignKey(LinkTable, db_column='otslinkid')
    spannumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oms_circuit_span_table'


class Ons15216ActiveUserTable(models.Model):
    nedbaccessid = models.IntegerField()
    userid = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'ons15216_active_user_table'
        unique_together = (('nedbaccessid', 'userid'),)


class Ons15216NeInventoryTable(models.Model):
    nedbaccessid = models.IntegerField()
    cleicode = models.CharField(max_length=32, blank=True, null=True)
    partnumber = models.CharField(max_length=32, blank=True, null=True)
    serialnumber = models.CharField(max_length=32, blank=True, null=True)
    fwversion = models.CharField(max_length=32, blank=True, null=True)
    fwupdatedate = models.CharField(max_length=32, blank=True, null=True)
    wavelength = models.CharField(max_length=64, blank=True, null=True)
    modulenumber = models.BigIntegerField()
    macaddress = models.CharField(max_length=17, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15216_ne_inventory_table'
        unique_together = (('nedbaccessid', 'modulenumber'),)


class Ons15216PrivilegeTable(models.Model):
    privilegeid = models.IntegerField(primary_key=True)
    privilege = models.CharField(max_length=30)
    description = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15216_privilege_table'


class Ons15216UserTable(models.Model):
    nedbaccessid = models.IntegerField()
    userid = models.CharField(max_length=64)
    password = models.CharField(max_length=64, blank=True, null=True)
    privilegeid = models.ForeignKey(Ons15216PrivilegeTable, db_column='privilegeid', blank=True, null=True)
    lastlogintime = models.DateField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15216_user_table'
        unique_together = (('nedbaccessid', 'userid'),)


class Ons1530XHoPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    nebbe = models.CharField(max_length=40, blank=True, null=True)
    nees = models.CharField(max_length=40, blank=True, null=True)
    neses = models.CharField(max_length=40, blank=True, null=True)
    neuas = models.CharField(max_length=40, blank=True, null=True)
    febbe = models.CharField(max_length=40, blank=True, null=True)
    fees = models.CharField(max_length=40, blank=True, null=True)
    feses = models.CharField(max_length=40, blank=True, null=True)
    feuas = models.CharField(max_length=40, blank=True, null=True)
    objecttype = models.IntegerField()
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    is24h = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ons1530x_ho_pm_table'
        unique_together = (('nedbaccessid', 'moduletype', 'physicalloc', 'timestamp', 'neifindex', 'objecttype', 'is24h'),)


class Ons1530XIpPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    ifinucastpkts = models.CharField(max_length=40, blank=True, null=True)
    ifindiscards = models.CharField(max_length=40, blank=True, null=True)
    ifinerrors = models.CharField(max_length=40, blank=True, null=True)
    ifinoctets = models.CharField(max_length=40, blank=True, null=True)
    ifoutoctets = models.CharField(max_length=40, blank=True, null=True)
    ifinnucastpkts = models.CharField(max_length=40, blank=True, null=True)
    ifinunknownprotos = models.CharField(max_length=40, blank=True, null=True)
    ifoutucastpkts = models.CharField(max_length=40, blank=True, null=True)
    ifoutnucastpkts = models.CharField(max_length=40, blank=True, null=True)
    ifoutdiscards = models.CharField(max_length=40, blank=True, null=True)
    ifouterrors = models.CharField(max_length=40, blank=True, null=True)
    ifinmulticastpkts = models.CharField(max_length=40, blank=True, null=True)
    ifinbroadcastpkts = models.CharField(max_length=40, blank=True, null=True)
    ifoutmulticastpkts = models.CharField(max_length=40, blank=True, null=True)
    ifoutbroadcastpkts = models.CharField(max_length=40, blank=True, null=True)
    iftype = models.BooleanField()
    objecttype = models.IntegerField()
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    is24h = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ons1530x_ip_pm_table'
        unique_together = (('nedbaccessid', 'moduletype', 'physicalloc', 'timestamp', 'neifindex', 'objecttype', 'is24h'),)


class Ons1530XLoPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    nebbe = models.CharField(max_length=40, blank=True, null=True)
    nees = models.CharField(max_length=40, blank=True, null=True)
    neses = models.CharField(max_length=40, blank=True, null=True)
    neuas = models.CharField(max_length=40, blank=True, null=True)
    febbe = models.CharField(max_length=40, blank=True, null=True)
    fees = models.CharField(max_length=40, blank=True, null=True)
    feses = models.CharField(max_length=40, blank=True, null=True)
    feuas = models.CharField(max_length=40, blank=True, null=True)
    objecttype = models.IntegerField()
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    is24h = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ons1530x_lo_pm_table'
        unique_together = (('nedbaccessid', 'moduletype', 'physicalloc', 'timestamp', 'neifindex', 'objecttype', 'is24h'),)


class Ons1530XMsPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    nebbe = models.CharField(max_length=40, blank=True, null=True)
    nees = models.CharField(max_length=40, blank=True, null=True)
    neses = models.CharField(max_length=40, blank=True, null=True)
    neuas = models.CharField(max_length=40, blank=True, null=True)
    febbe = models.CharField(max_length=40, blank=True, null=True)
    fees = models.CharField(max_length=40, blank=True, null=True)
    feses = models.CharField(max_length=40, blank=True, null=True)
    feuas = models.CharField(max_length=40, blank=True, null=True)
    objecttype = models.IntegerField()
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    is24h = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ons1530x_ms_pm_table'
        unique_together = (('nedbaccessid', 'moduletype', 'physicalloc', 'timestamp', 'neifindex', 'objecttype', 'is24h'),)


class Ons1530XNeInventoryTable(models.Model):
    nedbaccessid = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    physicalloc = models.BigIntegerField()
    modulename = models.IntegerField(blank=True, null=True)
    servicestate = models.CharField(max_length=40, blank=True, null=True)
    softwareversion = models.CharField(max_length=16, blank=True, null=True)
    serialnumber = models.CharField(max_length=16, blank=True, null=True)
    hardwareversion = models.CharField(max_length=16, blank=True, null=True)
    installstate = models.CharField(max_length=40, blank=True, null=True)
    expectedmodule = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons1530x_ne_inventory_table'
        unique_together = (('nedbaccessid', 'physicalloc'),)


class Ons1530XRsPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    nebbe = models.CharField(max_length=40, blank=True, null=True)
    nees = models.CharField(max_length=40, blank=True, null=True)
    neses = models.CharField(max_length=40, blank=True, null=True)
    neuas = models.CharField(max_length=40, blank=True, null=True)
    objecttype = models.IntegerField()
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    is24h = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ons1530x_rs_pm_table'
        unique_together = (('nedbaccessid', 'moduletype', 'physicalloc', 'timestamp', 'neifindex', 'objecttype', 'is24h'),)


class Ons15454327NeTable(models.Model):
    nedbaccessid = models.IntegerField(primary_key=True)
    neaudittrailstatus = models.NullBooleanField()
    neaudittraillastsequencenumber = models.IntegerField(blank=True, null=True)
    nelastaudittrailcollectedtime = models.DateField(blank=True, null=True)
    nedwdmconfigmode = models.IntegerField(blank=True, null=True)
    last15minpmcollectedtime = models.DateField(blank=True, null=True)
    last1daypmcollectedtime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_327_ne_table'


class Ons154548B10BPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    validpackets = models.BigIntegerField(blank=True, null=True)
    invalidpackets = models.BigIntegerField(blank=True, null=True)
    codegroupviolations = models.BigIntegerField(blank=True, null=True)
    idleorderedsets = models.BigIntegerField(blank=True, null=True)
    nonidleorderedsets = models.BigIntegerField(blank=True, null=True)
    datacodegroups = models.BigIntegerField(blank=True, null=True)
    rxtotalpackets = models.BigIntegerField(blank=True, null=True)
    ifinerrors = models.BigIntegerField(blank=True, null=True)
    statsencodingdisperrors = models.BigIntegerField(blank=True, null=True)
    dataorderedsets = models.BigIntegerField(blank=True, null=True)
    datapayload = models.CharField(max_length=1024, blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    invalidorderedsets = models.BigIntegerField(blank=True, null=True)
    invldordrdsetdisperrorsum = models.BigIntegerField(blank=True, null=True)
    rx8b10bwords = models.BigIntegerField(blank=True, null=True)
    tx8b10bwords = models.BigIntegerField(blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_8b10b_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454ActiveUserTable(models.Model):
    nedbaccessid = models.IntegerField()
    userid = models.CharField(max_length=64)
    clientip = models.CharField(max_length=64)
    sessiontype = models.CharField(max_length=20, blank=True, null=True)
    lastlogintime = models.DateField(blank=True, null=True)
    lastactivitytime = models.DateField(blank=True, null=True)
    sessionticket = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons15454_active_user_table'
        unique_together = (('nedbaccessid', 'userid', 'clientip', 'sessionticket'),)


class Ons15454CbqosInfoTable(models.Model):
    nedbaccessid = models.IntegerField()
    physicalloc = models.BigIntegerField()
    moduletype = models.IntegerField(blank=True, null=True)
    cbqospolicyindex = models.IntegerField()
    cbqosobjectindex = models.IntegerField()
    cbqosconfigindex = models.IntegerField()
    cbqosobjecttype = models.IntegerField(blank=True, null=True)
    cbqosparentindex = models.IntegerField()
    objectname = models.CharField(max_length=4000, blank=True, null=True)
    displaystring = models.CharField(max_length=4000, blank=True, null=True)
    statsenabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ons15454_cbqos_info_table'
        unique_together = (('nedbaccessid', 'physicalloc', 'cbqospolicyindex', 'cbqosobjectindex'),)


class Ons15454CosPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    interfacename = models.CharField(max_length=40)
    interfacedirection = models.CharField(max_length=40)
    classofservicelevel = models.BooleanField()
    postpolicypackets = models.BigIntegerField(blank=True, null=True)
    postpolicybytes = models.BigIntegerField(blank=True, null=True)
    droppackets = models.BigIntegerField(blank=True, null=True)
    dropbytes = models.BigIntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_cos_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'interfacename', 'interfacedirection', 'classofservicelevel', 'is24h', 'neifpmstatus'),)


class Ons15454Ds1PmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    ds1linecodeviolations = models.IntegerField(blank=True, null=True)
    ds1lineerrsecs = models.IntegerField(blank=True, null=True)
    ds1lineseverrsecs = models.IntegerField(blank=True, null=True)
    ds1rxpathais = models.IntegerField(blank=True, null=True)
    ds1rxpatherrsecs = models.IntegerField(blank=True, null=True)
    ds1rxpathsas = models.IntegerField(blank=True, null=True)
    ds1rxpathseverrsecs = models.IntegerField(blank=True, null=True)
    ds1rxpathunavailablesecs = models.IntegerField(blank=True, null=True)
    ds1rxpathcodeviolations = models.IntegerField(blank=True, null=True)
    ds1txpathais = models.IntegerField(blank=True, null=True)
    ds1txpatherrsecs = models.IntegerField(blank=True, null=True)
    ds1txpathsas = models.IntegerField(blank=True, null=True)
    ds1txpathseverrsecs = models.IntegerField(blank=True, null=True)
    ds1txpathunavailablesecs = models.IntegerField(blank=True, null=True)
    ds1txpathcodeviolations = models.IntegerField(blank=True, null=True)
    ds1lineloss = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    feds1fdlpathcv = models.IntegerField(blank=True, null=True)
    feds1fdlpathes = models.IntegerField(blank=True, null=True)
    feds1fdlpathesa = models.IntegerField(blank=True, null=True)
    feds1fdlpathesb = models.IntegerField(blank=True, null=True)
    feds1fdlpathses = models.IntegerField(blank=True, null=True)
    feds1fdlpathsefs = models.IntegerField(blank=True, null=True)
    feds1fdlpathcss = models.IntegerField(blank=True, null=True)
    feds1fdlpathuas = models.IntegerField(blank=True, null=True)
    feds1fdlpathfc = models.IntegerField(blank=True, null=True)
    feds1fdllinees = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    feds1fdlesnp = models.IntegerField(blank=True, null=True)
    feds1fdlsesnp = models.IntegerField(blank=True, null=True)
    feds1fdluasnp = models.IntegerField(blank=True, null=True)
    ds1esnp = models.IntegerField(blank=True, null=True)
    ds1sesnp = models.IntegerField(blank=True, null=True)
    ds1uasnp = models.IntegerField(blank=True, null=True)
    ds1rxpathbbe = models.IntegerField(blank=True, null=True)
    ds1rxpathesr = models.IntegerField(blank=True, null=True)
    ds1rxpathsesr = models.IntegerField(blank=True, null=True)
    ds1rxpathbber = models.IntegerField(blank=True, null=True)
    ds1txpathbbe = models.IntegerField(blank=True, null=True)
    ds1txpathesr = models.IntegerField(blank=True, null=True)
    ds1txpathsesr = models.IntegerField(blank=True, null=True)
    ds1txpathbber = models.IntegerField(blank=True, null=True)
    ds1rxpathfc = models.IntegerField(blank=True, null=True)
    feds1fdlpathesr = models.IntegerField(blank=True, null=True)
    feds1fdlpathsesr = models.IntegerField(blank=True, null=True)
    ds1txpathfc = models.IntegerField(blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_ds1_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454Ds3PmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    ds3linecodeviolations = models.IntegerField(blank=True, null=True)
    ds3lineerrsecs = models.IntegerField(blank=True, null=True)
    ds3lineseverrsecs = models.IntegerField(blank=True, null=True)
    ds3lineloss = models.IntegerField(blank=True, null=True)
    ds3pbitais = models.IntegerField(blank=True, null=True)
    ds3pbitcodeviolations = models.IntegerField(blank=True, null=True)
    ds3pbiterrsecs = models.IntegerField(blank=True, null=True)
    ds3pbitsas = models.IntegerField(blank=True, null=True)
    ds3pbitseverrsecs = models.IntegerField(blank=True, null=True)
    ds3pbitunavailablesecs = models.IntegerField(blank=True, null=True)
    ds3cpbitcodeviolations = models.IntegerField(blank=True, null=True)
    ds3cpbiterrsecs = models.IntegerField(blank=True, null=True)
    ds3cpbitsas = models.IntegerField(blank=True, null=True)
    ds3cpbitseverrsecs = models.IntegerField(blank=True, null=True)
    ds3cpbitunavailablesecs = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    feds3cpbitcodeviolations = models.IntegerField(blank=True, null=True)
    feds3cpbiterrsecs = models.IntegerField(blank=True, null=True)
    feds3cpbitsas = models.IntegerField(blank=True, null=True)
    feds3cpbitseverrsecs = models.IntegerField(blank=True, null=True)
    feds3cpbitunavailablesecs = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_ds3_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454EnetPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    ifinoctets = models.BigIntegerField(blank=True, null=True)
    ifinucastpkts = models.BigIntegerField(blank=True, null=True)
    ifinmulticastpkts = models.BigIntegerField(blank=True, null=True)
    ifinbroadcastpkts = models.BigIntegerField(blank=True, null=True)
    ifinerrors = models.BigIntegerField(blank=True, null=True)
    ifoutoctets = models.BigIntegerField(blank=True, null=True)
    ifoutucastpkts = models.BigIntegerField(blank=True, null=True)
    ifoutmulticastpkts = models.BigIntegerField(blank=True, null=True)
    ifoutbroadcastpkts = models.BigIntegerField(blank=True, null=True)
    dot3statsalignmenterrors = models.BigIntegerField(blank=True, null=True)
    dot3statsfcserrors = models.BigIntegerField(blank=True, null=True)
    dot3statssinglecollisionframes = models.BigIntegerField(blank=True, null=True)
    dot3statsmulticollisionframes = models.BigIntegerField(blank=True, null=True)
    dot3statsdeferredtransmissions = models.BigIntegerField(blank=True, null=True)
    dot3statslatecollisions = models.BigIntegerField(blank=True, null=True)
    dot3statsexcessivecollisions = models.BigIntegerField(blank=True, null=True)
    etherstatsundersizepkts = models.BigIntegerField(blank=True, null=True)
    etherstatsfragments = models.BigIntegerField(blank=True, null=True)
    etherstatsoversizepkts = models.BigIntegerField(blank=True, null=True)
    etherstatsjabbers = models.BigIntegerField(blank=True, null=True)
    rxpauseframes = models.BigIntegerField(blank=True, null=True)
    txpauseframes = models.BigIntegerField(blank=True, null=True)
    rxpktsdropinternalcongestion = models.BigIntegerField(blank=True, null=True)
    txpktsdropinternalcongestion = models.BigIntegerField(blank=True, null=True)
    rxpackets = models.BigIntegerField(blank=True, null=True)
    txpackets = models.BigIntegerField(blank=True, null=True)
    rxtotalerrors = models.BigIntegerField(blank=True, null=True)
    rxrunts = models.BigIntegerField(blank=True, null=True)
    rxgiants = models.BigIntegerField(blank=True, null=True)
    txcollisions = models.BigIntegerField(blank=True, null=True)
    rxgmacdropcounts = models.BigIntegerField(blank=True, null=True)
    rxthresholdoversizes = models.BigIntegerField(blank=True, null=True)
    portdropcounts = models.BigIntegerField(blank=True, null=True)
    txgiants = models.BigIntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    etherutilizationstats = models.IntegerField(blank=True, null=True)
    hdlcpktdrops = models.BigIntegerField(blank=True, null=True)
    rxcontrolframes = models.BigIntegerField(blank=True, null=True)
    rxunknownopcodeframes = models.BigIntegerField(blank=True, null=True)
    ifinerrorbytepkts = models.BigIntegerField(blank=True, null=True)
    ifinframingerrorpkts = models.BigIntegerField(blank=True, null=True)
    ifinjunkinterpkts = models.BigIntegerField(blank=True, null=True)
    ifindiscards = models.BigIntegerField(blank=True, null=True)
    ifoutdiscards = models.BigIntegerField(blank=True, null=True)
    dot3statsframetoolong = models.BigIntegerField(blank=True, null=True)
    dot3statscarriersenseerrors = models.BigIntegerField(blank=True, null=True)
    dot3statssqetesterrors = models.BigIntegerField(blank=True, null=True)
    etherstatspkts64octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts65to127octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts128to255octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts256to511octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts512to1023octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts1024to1518octets = models.BigIntegerField(blank=True, null=True)
    etherstatsbroadcastpkts = models.BigIntegerField(blank=True, null=True)
    etherstatsmulticastpkts = models.BigIntegerField(blank=True, null=True)
    etherstatsoctets = models.BigIntegerField(blank=True, null=True)
    etherstatscollisions = models.BigIntegerField(blank=True, null=True)
    etherstatscollisionframes = models.BigIntegerField(blank=True, null=True)
    etherstatscrcalignerrors = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframestruncated = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframestoolong = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframesbadcrc = models.BigIntegerField(blank=True, null=True)
    mediaindstatstxframesbadcrc = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxshortpkts = models.BigIntegerField(blank=True, null=True)
    mediaindstatsoversizedropped = models.BigIntegerField(blank=True, null=True)
    ifouterrors = models.BigIntegerField(blank=True, null=True)
    etherstatspkts = models.BigIntegerField(blank=True, null=True)
    dot3statsinternalmactxerrors = models.BigIntegerField(blank=True, null=True)
    dot3statsinternalmacrxerrors = models.BigIntegerField(blank=True, null=True)
    dot3statssymbolerrors = models.BigIntegerField(blank=True, null=True)
    mediaindstatstxframestoolong = models.BigIntegerField(blank=True, null=True)
    rxetherutilizationstats = models.IntegerField(blank=True, null=True)
    txetherutilizationstats = models.IntegerField(blank=True, null=True)
    statslinelastclearedtime = models.DateField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    dot3statsctrinunknownopcodes = models.BigIntegerField(blank=True, null=True)
    dot3statsinpauseframes = models.BigIntegerField(blank=True, null=True)
    dot3statsoutpauseframes = models.BigIntegerField(blank=True, null=True)
    etherstatspkts1519to1522octets = models.BigIntegerField(blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)
    etherstatstxfifooverflowevents = models.BigIntegerField(blank=True, null=True)
    ifhcinoctets = models.BigIntegerField(blank=True, null=True)
    ifhcinucastpkts = models.BigIntegerField(blank=True, null=True)
    ifhcinmulticastpkts = models.BigIntegerField(blank=True, null=True)
    ifhcinbroadcastpkts = models.BigIntegerField(blank=True, null=True)
    ifhcoutoctets = models.BigIntegerField(blank=True, null=True)
    ifhcoutmulticastpkts = models.BigIntegerField(blank=True, null=True)
    ifhcoutbroadcastpkts = models.BigIntegerField(blank=True, null=True)
    etherstatshighcapacitypkts = models.BigIntegerField(blank=True, null=True)
    etherstatshighcapacityoctets = models.BigIntegerField(blank=True, null=True)
    etherstatshc64octets = models.BigIntegerField(blank=True, null=True)
    etherstatshc65to127octets = models.BigIntegerField(blank=True, null=True)
    etherstatshc128to255octets = models.BigIntegerField(blank=True, null=True)
    etherstatshc256to511octets = models.BigIntegerField(blank=True, null=True)
    etherstatshc512to1023octets = models.BigIntegerField(blank=True, null=True)
    etherstatshc1024to1518octets = models.BigIntegerField(blank=True, null=True)
    cisrxreports = models.BigIntegerField(blank=True, null=True)
    cisrxleaves = models.BigIntegerField(blank=True, null=True)
    cistxreports = models.BigIntegerField(blank=True, null=True)
    cistxleaves = models.BigIntegerField(blank=True, null=True)
    cistxgeneralqueries = models.BigIntegerField(blank=True, null=True)
    cistxgroupspecificqueries = models.BigIntegerField(blank=True, null=True)
    cisrxgeneralqueries = models.BigIntegerField(blank=True, null=True)
    cisrxgroupspecificqueries = models.BigIntegerField(blank=True, null=True)
    cisrxvalidpackets = models.BigIntegerField(blank=True, null=True)
    cisrxinvalidpackets = models.BigIntegerField(blank=True, null=True)
    dot3adaggportstatslacpdusrx = models.BigIntegerField(blank=True, null=True)
    dot3adaggportstatslacpdustx = models.BigIntegerField(blank=True, null=True)
    crephflrxpdus = models.BigIntegerField(blank=True, null=True)
    crephfltxpdus = models.BigIntegerField(blank=True, null=True)
    creplslrxpdus = models.BigIntegerField(blank=True, null=True)
    creplsltxpdus = models.BigIntegerField(blank=True, null=True)
    etherstatspkts1519tomaxoctets = models.BigIntegerField(blank=True, null=True)
    mediaindstatstxshortpkts = models.BigIntegerField(blank=True, null=True)
    dot3statslcverrors = models.BigIntegerField(blank=True, null=True)
    dot3statslayer1errors = models.BigIntegerField(blank=True, null=True)
    pcserrcount = models.BigIntegerField(blank=True, null=True)
    pcs49rxerrber = models.BigIntegerField(blank=True, null=True)
    pcs49errdec = models.BigIntegerField(blank=True, null=True)
    pcserrcount2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_enet_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454FcPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    fibrestatsinvalidorderedsets = models.BigIntegerField(blank=True, null=True)
    fibrestatsencodingdisperrors = models.BigIntegerField(blank=True, null=True)
    fibrestatsrxtotalerrors = models.BigIntegerField(blank=True, null=True)
    fibrestatsrxframestruncated = models.BigIntegerField(blank=True, null=True)
    fibrestatsrxframestoolong = models.BigIntegerField(blank=True, null=True)
    fibrestatsrxframesbadcrc = models.BigIntegerField(blank=True, null=True)
    fibrestatsrxframes = models.BigIntegerField(blank=True, null=True)
    fibrestatsrxoctets = models.BigIntegerField(blank=True, null=True)
    fibrestatsrxdiscards = models.BigIntegerField(blank=True, null=True)
    fibrestatstxframesbadcrc = models.BigIntegerField(blank=True, null=True)
    fibrestatstxframes = models.BigIntegerField(blank=True, null=True)
    fibrestatstxoctets = models.BigIntegerField(blank=True, null=True)
    fibrestatstxdiscards = models.BigIntegerField(blank=True, null=True)
    fibrestatslinkresets = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxsbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxmbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxtypeinvalid = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxsblkcrcerrors = models.BigIntegerField(blank=True, null=True)
    rxfcutilizationstats = models.IntegerField(blank=True, null=True)
    txfcutilizationstats = models.IntegerField(blank=True, null=True)
    statslinelastclearedtime = models.DateField(blank=True, null=True)
    gfpstatscsfraised = models.BigIntegerField(blank=True, null=True)
    gfpstatsroundtriplatency = models.BigIntegerField(blank=True, null=True)
    ifinerrors = models.BigIntegerField(blank=True, null=True)
    fibrestatslinkrecoveries = models.BigIntegerField(blank=True, null=True)
    fcingressrxdistanceextbuffers = models.BigIntegerField(blank=True, null=True)
    fcegresstxdistanceextbuffers = models.BigIntegerField(blank=True, null=True)
    fibrestatsrxcredits = models.BigIntegerField(blank=True, null=True)
    fibrestatstxcredits = models.BigIntegerField(blank=True, null=True)
    fibrestatszerotxcredits = models.BigIntegerField(blank=True, null=True)
    txpackets = models.BigIntegerField(blank=True, null=True)
    rxpackets = models.BigIntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    fibrestatsrxrecvrready = models.BigIntegerField(blank=True, null=True)
    fibrestatstxrecvrready = models.BigIntegerField(blank=True, null=True)
    invldordrdsetdisperrorsum = models.BigIntegerField(blank=True, null=True)
    ifoutoversizepkts = models.BigIntegerField(blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)
    fibrestatstxframestruncated = models.BigIntegerField(blank=True, null=True)
    fibrestatstxframestoolong = models.BigIntegerField(blank=True, null=True)
    ifouterrors = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxlcverrors = models.BigIntegerField(blank=True, null=True)
    mediaindstatstxlcverrors = models.BigIntegerField(blank=True, null=True)
    pcs49rxerrber = models.BigIntegerField(blank=True, null=True)
    pcs49errdec = models.BigIntegerField(blank=True, null=True)
    pcsegrxerrframes = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_fc_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454GfpPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    gfpstatscsfraised = models.BigIntegerField(blank=True, null=True)
    gfpstatslfdraised = models.BigIntegerField(blank=True, null=True)
    gfpstatsroundtriplatency = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxcidinvalid = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxcrcerrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxframe = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxmbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxoctets = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxsbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxsblkcrcerrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxtypeinvalid = models.BigIntegerField(blank=True, null=True)
    gfpstatstxframe = models.BigIntegerField(blank=True, null=True)
    gfpstatstxoctets = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxdistanceextbuffers = models.BigIntegerField(blank=True, null=True)
    gfpstatstxdistanceextbuffers = models.BigIntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)
    gfprxcmfframe = models.BigIntegerField(blank=True, null=True)
    gfptxcmfframe = models.BigIntegerField(blank=True, null=True)
    ifinpayloadcrcerrors = models.BigIntegerField(blank=True, null=True)
    gfpstatschecrxmbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsthecrxmbiterrors = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_gfp_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454InventoryNotes(models.Model):
    serialnumber = models.CharField(primary_key=True, max_length=16)
    note = models.CharField(max_length=4000, blank=True, null=True)
    inserted = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_inventory_notes'


class Ons15454IpslaPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    rttmonstatsstarttimeindex = models.BigIntegerField(blank=True, null=True)
    rttmonstatscompletions = models.BigIntegerField(blank=True, null=True)
    rttmonstatsoverthresholds = models.BigIntegerField(blank=True, null=True)
    rttmonstatsnumofrtt = models.BigIntegerField(blank=True, null=True)
    rttmonstatsrttsum = models.BigIntegerField(blank=True, null=True)
    rttmonstatsrttsum2low = models.BigIntegerField(blank=True, null=True)
    rttmonstatsrttsum2high = models.BigIntegerField(blank=True, null=True)
    rttmonstatsrttmin = models.BigIntegerField(blank=True, null=True)
    rttmonstatsrttmax = models.BigIntegerField(blank=True, null=True)
    rttmonstatsminofpositivessd = models.BigIntegerField(blank=True, null=True)
    rttmonstatsmaxofpositivessd = models.BigIntegerField(blank=True, null=True)
    rttmonstatsnumofpositivessd = models.BigIntegerField(blank=True, null=True)
    rttmonstatssumofpositivessd = models.BigIntegerField(blank=True, null=True)
    rttmonstatssum2positivessdlow = models.BigIntegerField(blank=True, null=True)
    rttmonstatssum2positivessdhigh = models.BigIntegerField(blank=True, null=True)
    rttmonstatsminofnegativessd = models.BigIntegerField(blank=True, null=True)
    rttmonstatsmaxofnegativessd = models.BigIntegerField(blank=True, null=True)
    rttmonstatsnumofnegativessd = models.BigIntegerField(blank=True, null=True)
    rttmonstatssumofnegativessd = models.BigIntegerField(blank=True, null=True)
    rttmonstatssum2negativessdlow = models.BigIntegerField(blank=True, null=True)
    rttmonstatssum2negativessdhigh = models.BigIntegerField(blank=True, null=True)
    rttmonstatsminofpositivesds = models.BigIntegerField(blank=True, null=True)
    rttmonstatsmaxofpositivesds = models.BigIntegerField(blank=True, null=True)
    rttmonstatsnumofpositivesds = models.BigIntegerField(blank=True, null=True)
    rttmonstatssumofpositivesds = models.BigIntegerField(blank=True, null=True)
    rttmonstatssum2positivesdslow = models.BigIntegerField(blank=True, null=True)
    rttmonstatssum2positivesdshigh = models.BigIntegerField(blank=True, null=True)
    rttmonstatsminofnegativesds = models.BigIntegerField(blank=True, null=True)
    rttmonstatsmaxofnegativesds = models.BigIntegerField(blank=True, null=True)
    rttmonstatsnumofnegativesds = models.BigIntegerField(blank=True, null=True)
    rttmonstatssumofnegativesds = models.BigIntegerField(blank=True, null=True)
    rttmonstatssum2negativesdslow = models.BigIntegerField(blank=True, null=True)
    rttmonstatssum2negativesdshigh = models.BigIntegerField(blank=True, null=True)
    rttmonstatspacketlosssd = models.BigIntegerField(blank=True, null=True)
    rttmonstatspacketlossds = models.BigIntegerField(blank=True, null=True)
    rttmonstatspacketoutofsequence = models.BigIntegerField(blank=True, null=True)
    rttmonstatspacketmia = models.BigIntegerField(blank=True, null=True)
    rttmonstatspacketlatearrival = models.BigIntegerField(blank=True, null=True)
    rttmonstatserror = models.BigIntegerField(blank=True, null=True)
    rttmonstatsbusies = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowsumsd = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowsum2sdlow = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowsum2sdhigh = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowminsd = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowmaxsd = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowsumds = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowsum2dslow = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowsum2dshigh = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowminds = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowmaxds = models.BigIntegerField(blank=True, null=True)
    rttmonstatsnumofow = models.BigIntegerField(blank=True, null=True)
    rttmonstatsowminsdnew = models.BigIntegerField(blank=True, null=True)
    statslinelastclearedtime = models.DateField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_ipsla_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454LagPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    interfacename = models.CharField(max_length=40)
    lacpdusrx = models.BigIntegerField(blank=True, null=True)
    markerpdusrx = models.BigIntegerField(blank=True, null=True)
    markerresponsepdusrx = models.BigIntegerField(blank=True, null=True)
    unknownrx = models.BigIntegerField(blank=True, null=True)
    illegalrx = models.BigIntegerField(blank=True, null=True)
    lacpdustx = models.BigIntegerField(blank=True, null=True)
    markerpdustx = models.BigIntegerField(blank=True, null=True)
    markerresponsepdustx = models.BigIntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_lag_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'interfacename', 'is24h', 'neifpmstatus'),)


class Ons15454NeInventoryTable(models.Model):
    nedbaccessid = models.IntegerField()
    physicalloc = models.BigIntegerField()
    equipmenttype = models.IntegerField(blank=True, null=True)
    adminstate = models.CharField(max_length=32, blank=True, null=True)
    servicestate = models.CharField(max_length=150, blank=True, null=True)
    actualequipmenttype = models.IntegerField(blank=True, null=True)
    hwpartnumber = models.CharField(max_length=16, blank=True, null=True)
    serialnumber = models.CharField(max_length=16, blank=True, null=True)
    manufacturingdate = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    applicationfilename = models.CharField(max_length=30, blank=True, null=True)
    extrainfo = models.CharField(max_length=4000, blank=True, null=True)
    firmwareversion = models.CharField(max_length=16, blank=True, null=True)
    equipmentstate = models.NullBooleanField()
    entityid = models.IntegerField()
    hardwarerevision = models.CharField(max_length=7, blank=True, null=True)
    cleicode = models.CharField(max_length=30, blank=True, null=True)
    inventorycode = models.CharField(max_length=40, blank=True, null=True)
    productid = models.CharField(max_length=40, blank=True, null=True)
    versionid = models.CharField(max_length=20, blank=True, null=True)
    lastinterfacechange = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_ne_inventory_table'
        unique_together = (('nedbaccessid', 'physicalloc', 'entityid'),)


class Ons15454OtnFecPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    biterrscorrected = models.BigIntegerField(blank=True, null=True)
    byteerrscorrected = models.BigIntegerField(blank=True, null=True)
    zerobiterrsdetected = models.BigIntegerField(blank=True, null=True)
    onebiterrsdetected = models.BigIntegerField(blank=True, null=True)
    uncorrectableword = models.BigIntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)
    prefecber = models.FloatField(blank=True, null=True)
    seqmism = models.BigIntegerField(blank=True, null=True)
    backautherr = models.BigIntegerField(blank=True, null=True)
    autherr = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_otn_fec_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454OtnPathPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    errsecs = models.IntegerField(blank=True, null=True)
    severrsecs = models.IntegerField(blank=True, null=True)
    unavailablesecs = models.IntegerField(blank=True, null=True)
    backgroundblockerr = models.IntegerField(blank=True, null=True)
    failurecount = models.IntegerField(blank=True, null=True)
    errsecsratio = models.IntegerField(blank=True, null=True)
    severrsecsratio = models.IntegerField(blank=True, null=True)
    backgroundblockerrratio = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    feerrsecs = models.IntegerField(blank=True, null=True)
    feseverrsecs = models.IntegerField(blank=True, null=True)
    feunavailablesecs = models.IntegerField(blank=True, null=True)
    febackgroundblockerrs = models.IntegerField(blank=True, null=True)
    fefailurecount = models.IntegerField(blank=True, null=True)
    feerrsecsratio = models.IntegerField(blank=True, null=True)
    feseverrsecsratio = models.IntegerField(blank=True, null=True)
    febackgroundblockerrratio = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_otn_path_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454OtnSecPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    errsecs = models.IntegerField(blank=True, null=True)
    severrsecs = models.IntegerField(blank=True, null=True)
    unavailablesecs = models.IntegerField(blank=True, null=True)
    backgroundblockerr = models.IntegerField(blank=True, null=True)
    failurecount = models.IntegerField(blank=True, null=True)
    errsecsratio = models.IntegerField(blank=True, null=True)
    severrsecsratio = models.IntegerField(blank=True, null=True)
    backgroundblockerrratio = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    feerrsecs = models.IntegerField(blank=True, null=True)
    feseverrsecs = models.IntegerField(blank=True, null=True)
    feunavailablesecs = models.IntegerField(blank=True, null=True)
    febackgroundblockerrs = models.IntegerField(blank=True, null=True)
    fefailurecount = models.IntegerField(blank=True, null=True)
    feerrsecsratio = models.IntegerField(blank=True, null=True)
    feseverrsecsratio = models.IntegerField(blank=True, null=True)
    febackgroundblockerrratio = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_otn_sec_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454PhyLayerPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    laserbiascurrent = models.IntegerField(blank=True, null=True)
    opticalpowertransmitted = models.IntegerField(blank=True, null=True)
    opticalpowerreceived = models.IntegerField(blank=True, null=True)
    minlaserbias = models.IntegerField(blank=True, null=True)
    avglaserbias = models.IntegerField(blank=True, null=True)
    maxlaserbias = models.IntegerField(blank=True, null=True)
    minlasertemp = models.IntegerField(blank=True, null=True)
    avglasertemp = models.IntegerField(blank=True, null=True)
    maxlasertemp = models.IntegerField(blank=True, null=True)
    minreceivedlasertemp = models.IntegerField(blank=True, null=True)
    avgreceivedlasertemp = models.IntegerField(blank=True, null=True)
    maxreceivedlasertemp = models.IntegerField(blank=True, null=True)
    mintransreceivervoltage = models.IntegerField(blank=True, null=True)
    avgtransreceivervoltage = models.IntegerField(blank=True, null=True)
    maxtransreceivervoltage = models.IntegerField(blank=True, null=True)
    mintransmittedpower = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    avgtransmittedpower = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxtransmittedpower = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    minreceivedpower = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    avgreceivedpower = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxreceivedpower = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    minpassthroughpower = models.IntegerField(blank=True, null=True)
    avgpassthroughpower = models.IntegerField(blank=True, null=True)
    maxpassthroughpower = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)
    mintxoscpower = models.IntegerField(blank=True, null=True)
    avgtxoscpower = models.IntegerField(blank=True, null=True)
    maxtxoscpower = models.IntegerField(blank=True, null=True)
    minrxoscpower = models.IntegerField(blank=True, null=True)
    avgrxoscpower = models.IntegerField(blank=True, null=True)
    maxrxoscpower = models.IntegerField(blank=True, null=True)
    minpmd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    avgpmd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxpmd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    minosnr = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    avgosnr = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxosnr = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cd = models.IntegerField(blank=True, null=True)
    minsopmd = models.IntegerField(blank=True, null=True)
    avgsopmd = models.IntegerField(blank=True, null=True)
    maxsopmd = models.IntegerField(blank=True, null=True)
    minpcr = models.IntegerField(blank=True, null=True)
    avgpcr = models.IntegerField(blank=True, null=True)
    maxpcr = models.IntegerField(blank=True, null=True)
    minpdl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    avgpdl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxpdl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    minpn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    avgpn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxpn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mincd = models.IntegerField(blank=True, null=True)
    avgcd = models.IntegerField(blank=True, null=True)
    maxcd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_phy_layer_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454PosPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    posstatsrxprehdlcbytes = models.BigIntegerField(blank=True, null=True)
    posstatsrxposthdlcbytes = models.BigIntegerField(blank=True, null=True)
    posstatsrxpackets = models.BigIntegerField(blank=True, null=True)
    posstatsrxnormalpackets = models.BigIntegerField(blank=True, null=True)
    posstatsrxshorts = models.BigIntegerField(blank=True, null=True)
    posstatsrxrunts = models.BigIntegerField(blank=True, null=True)
    posstatsrxlongs = models.BigIntegerField(blank=True, null=True)
    posstatsrxtotalerrors = models.BigIntegerField(blank=True, null=True)
    posstatsrxcrcerrors = models.BigIntegerField(blank=True, null=True)
    posstatsrxinputdroppackets = models.BigIntegerField(blank=True, null=True)
    posstatsrxinputabortpackets = models.BigIntegerField(blank=True, null=True)
    posstatstxprehdlcbytes = models.BigIntegerField(blank=True, null=True)
    posstatstxposthdlcbytes = models.BigIntegerField(blank=True, null=True)
    posstatstxpackets = models.BigIntegerField(blank=True, null=True)
    posstatsdropcounts = models.BigIntegerField(blank=True, null=True)
    etherstatsdropevents = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxsbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxmbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxtypeinvalid = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxcrcerrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxcidinvalid = models.BigIntegerField(blank=True, null=True)
    gfpstatscsfraised = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxframe = models.BigIntegerField(blank=True, null=True)
    gfpstatstxframe = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxoctets = models.BigIntegerField(blank=True, null=True)
    gfpstatstxoctets = models.BigIntegerField(blank=True, null=True)
    gfpstatslfdraised = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframestruncated = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframestoolong = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframesbadcrc = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxshortpkts = models.BigIntegerField(blank=True, null=True)
    hdlcinoctets = models.BigIntegerField(blank=True, null=True)
    hdlcrxaborts = models.BigIntegerField(blank=True, null=True)
    hdlcoutoctets = models.BigIntegerField(blank=True, null=True)
    ifinoctets = models.BigIntegerField(blank=True, null=True)
    ifoutoctets = models.BigIntegerField(blank=True, null=True)
    rxpktsdropinternalcongestion = models.BigIntegerField(blank=True, null=True)
    ifindiscards = models.BigIntegerField(blank=True, null=True)
    rxetherutilizationstats = models.BigIntegerField(blank=True, null=True)
    txetherutilizationstats = models.BigIntegerField(blank=True, null=True)
    statslinelastclearedtime = models.DateField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    ifinpayloadcrcerrors = models.BigIntegerField(blank=True, null=True)
    ifoutpayloadcrcerrors = models.BigIntegerField(blank=True, null=True)
    ifoutoversizepackets = models.BigIntegerField(blank=True, null=True)
    hdlcpktdrops = models.BigIntegerField(blank=True, null=True)
    ifoutdiscards = models.BigIntegerField(blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_pos_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454PrivilegeTable(models.Model):
    privilegeid = models.IntegerField(primary_key=True)
    privilege = models.CharField(max_length=30)
    description = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_privilege_table'


class Ons15454RprPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    spaninucastclasscframes = models.BigIntegerField(blank=True, null=True)
    spaninucastclasscoctets = models.BigIntegerField(blank=True, null=True)
    spaninmcastclasscframes = models.BigIntegerField(blank=True, null=True)
    spaninmcastclasscoctets = models.BigIntegerField(blank=True, null=True)
    spaninucastclassbeirframes = models.BigIntegerField(blank=True, null=True)
    spaninucastclassbeiroctets = models.BigIntegerField(blank=True, null=True)
    spaninmcastclassbeirframes = models.BigIntegerField(blank=True, null=True)
    spaninmcastclassbeiroctets = models.BigIntegerField(blank=True, null=True)
    spaninucastclassbcirframes = models.BigIntegerField(blank=True, null=True)
    spaninucastclassbciroctets = models.BigIntegerField(blank=True, null=True)
    spaninmcastclassbcirframes = models.BigIntegerField(blank=True, null=True)
    spaninmcastclassbciroctets = models.BigIntegerField(blank=True, null=True)
    spaninucastclassaframes = models.BigIntegerField(blank=True, null=True)
    spaninucastclassaoctets = models.BigIntegerField(blank=True, null=True)
    spaninmcastclassaframes = models.BigIntegerField(blank=True, null=True)
    spaninmcastclassaoctets = models.BigIntegerField(blank=True, null=True)
    spaninctrlframes = models.BigIntegerField(blank=True, null=True)
    spaninoamechoframes = models.BigIntegerField(blank=True, null=True)
    spaninoamflushframes = models.BigIntegerField(blank=True, null=True)
    spaninoamorgframes = models.BigIntegerField(blank=True, null=True)
    spanintopoatdframes = models.BigIntegerField(blank=True, null=True)
    spanintopochksumframes = models.BigIntegerField(blank=True, null=True)
    spanintopotpframes = models.BigIntegerField(blank=True, null=True)
    spanoutucastclasscframes = models.BigIntegerField(blank=True, null=True)
    spanoutucastclasscoctets = models.BigIntegerField(blank=True, null=True)
    spanoutmcastclasscframes = models.BigIntegerField(blank=True, null=True)
    spanoutmcastclasscoctets = models.BigIntegerField(blank=True, null=True)
    spanoutucastclassbeirframes = models.BigIntegerField(blank=True, null=True)
    spanoutucastclassbeiroctets = models.BigIntegerField(blank=True, null=True)
    spanoutmcastclassbeirframes = models.BigIntegerField(blank=True, null=True)
    spanoutmcastclassbeiroctets = models.BigIntegerField(blank=True, null=True)
    spanoutucastclassbcirframes = models.BigIntegerField(blank=True, null=True)
    spanoutucastclassbciroctets = models.BigIntegerField(blank=True, null=True)
    spanoutmcastclassbcirframes = models.BigIntegerField(blank=True, null=True)
    spanoutmcastclassbciroctets = models.BigIntegerField(blank=True, null=True)
    spanoutucastclassaframes = models.BigIntegerField(blank=True, null=True)
    spanoutucastclassaoctets = models.BigIntegerField(blank=True, null=True)
    spanoutmcastclassaframes = models.BigIntegerField(blank=True, null=True)
    spanoutmcastclassaoctets = models.BigIntegerField(blank=True, null=True)
    spanoutctrlframes = models.BigIntegerField(blank=True, null=True)
    spanoutoamechoframes = models.BigIntegerField(blank=True, null=True)
    spanoutoamflushframes = models.BigIntegerField(blank=True, null=True)
    spanoutoamorgframes = models.BigIntegerField(blank=True, null=True)
    spanouttopoatdframes = models.BigIntegerField(blank=True, null=True)
    spanouttopochksumframes = models.BigIntegerField(blank=True, null=True)
    spanouttopotpframes = models.BigIntegerField(blank=True, null=True)
    clientinucastclasscframes = models.BigIntegerField(blank=True, null=True)
    clientinucastclasscoctets = models.BigIntegerField(blank=True, null=True)
    clientinmcastclasscframes = models.BigIntegerField(blank=True, null=True)
    clientinmcastclasscoctets = models.BigIntegerField(blank=True, null=True)
    clientinucastclassbeirframes = models.BigIntegerField(blank=True, null=True)
    clientinucastclassbeiroctets = models.BigIntegerField(blank=True, null=True)
    clientinmcastclassbeirframes = models.BigIntegerField(blank=True, null=True)
    clientinmcastclassbeiroctets = models.BigIntegerField(blank=True, null=True)
    clientinucastclassbcirframes = models.BigIntegerField(blank=True, null=True)
    clientinucastclassbciroctets = models.BigIntegerField(blank=True, null=True)
    clientinmcastclassbcirframes = models.BigIntegerField(blank=True, null=True)
    clientinmcastclassbciroctets = models.BigIntegerField(blank=True, null=True)
    clientinucastclassaframes = models.BigIntegerField(blank=True, null=True)
    clientinucastclassaoctets = models.BigIntegerField(blank=True, null=True)
    clientinmcastclassaframes = models.BigIntegerField(blank=True, null=True)
    clientinmcastclassaoctets = models.BigIntegerField(blank=True, null=True)
    clientinbcastframes = models.BigIntegerField(blank=True, null=True)
    clientoutucastclasscframes = models.BigIntegerField(blank=True, null=True)
    clientoutucastclasscoctets = models.BigIntegerField(blank=True, null=True)
    clientoutmcastclasscframes = models.BigIntegerField(blank=True, null=True)
    clientoutmcastclasscoctets = models.BigIntegerField(blank=True, null=True)
    clientoutucastclassbeirframes = models.BigIntegerField(blank=True, null=True)
    clientoutucastclassbeiroctets = models.BigIntegerField(blank=True, null=True)
    clientoutmcastclassbeirframes = models.BigIntegerField(blank=True, null=True)
    clientoutmcastclassbeiroctets = models.BigIntegerField(blank=True, null=True)
    clientoutucastclassbcirframes = models.BigIntegerField(blank=True, null=True)
    clientoutucastclassbciroctets = models.BigIntegerField(blank=True, null=True)
    clientoutmcastclassbcirframes = models.BigIntegerField(blank=True, null=True)
    clientoutmcastclassbciroctets = models.BigIntegerField(blank=True, null=True)
    clientoutucastclassaframes = models.BigIntegerField(blank=True, null=True)
    clientoutucastclassaoctets = models.BigIntegerField(blank=True, null=True)
    clientoutmcastclassaframes = models.BigIntegerField(blank=True, null=True)
    clientoutmcastclassaoctets = models.BigIntegerField(blank=True, null=True)
    clientoutbcastframes = models.BigIntegerField(blank=True, null=True)
    errorbadparityframes = models.BigIntegerField(blank=True, null=True)
    errorbadhecframes = models.BigIntegerField(blank=True, null=True)
    errorttlexpframes = models.BigIntegerField(blank=True, null=True)
    errortoolongframes = models.BigIntegerField(blank=True, null=True)
    errortooshortframes = models.BigIntegerField(blank=True, null=True)
    errorbadfcsframes = models.BigIntegerField(blank=True, null=True)
    errorselfsrcucastframes = models.BigIntegerField(blank=True, null=True)
    errorpmdabortframes = models.BigIntegerField(blank=True, null=True)
    errorbadaddrframes = models.BigIntegerField(blank=True, null=True)
    errorcontainedframes = models.BigIntegerField(blank=True, null=True)
    errorscfferrors = models.BigIntegerField(blank=True, null=True)
    portcountererror = models.BigIntegerField(blank=True, null=True)
    erroroversizeframes = models.BigIntegerField(blank=True, null=True)
    timelastcleared = models.DateField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_rpr_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SonetLinePmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    codeviolations = models.IntegerField(blank=True, null=True)
    errsecs = models.IntegerField(blank=True, null=True)
    severrsecs = models.IntegerField(blank=True, null=True)
    unavailablesecs = models.IntegerField(blank=True, null=True)
    ppjcpdet = models.IntegerField(blank=True, null=True)
    npjcpdet = models.IntegerField(blank=True, null=True)
    ppjcpgen = models.IntegerField(blank=True, null=True)
    npjcpgen = models.IntegerField(blank=True, null=True)
    fcl = models.IntegerField(blank=True, null=True)
    psc = models.IntegerField(blank=True, null=True)
    psd = models.IntegerField(blank=True, null=True)
    pjdiff = models.IntegerField(blank=True, null=True)
    pjpsec = models.IntegerField(blank=True, null=True)
    pjnsec = models.IntegerField(blank=True, null=True)
    pscw = models.IntegerField(blank=True, null=True)
    psdw = models.IntegerField(blank=True, null=True)
    pscr = models.IntegerField(blank=True, null=True)
    psdr = models.IntegerField(blank=True, null=True)
    pscs = models.IntegerField(blank=True, null=True)
    psds = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    fecodeviolations = models.IntegerField(blank=True, null=True)
    feerrsecs = models.IntegerField(blank=True, null=True)
    feseverrsecs = models.IntegerField(blank=True, null=True)
    feunavailablesecs = models.IntegerField(blank=True, null=True)
    fefcl = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_sonet_line_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SonetPathPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    sonetpathcodeviolations = models.IntegerField(blank=True, null=True)
    sonetpatherrsecs = models.IntegerField(blank=True, null=True)
    sonetpathseverrsecs = models.IntegerField(blank=True, null=True)
    sonetpathunavailablesecs = models.IntegerField(blank=True, null=True)
    sonetpathfc = models.IntegerField(blank=True, null=True)
    ppjcpdet = models.IntegerField(blank=True, null=True)
    npjcpdet = models.IntegerField(blank=True, null=True)
    ppjcpgen = models.IntegerField(blank=True, null=True)
    npjcpgen = models.IntegerField(blank=True, null=True)
    pjdiff = models.IntegerField(blank=True, null=True)
    pjpsec = models.IntegerField(blank=True, null=True)
    pjnsec = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    fesonetpathcodeviolations = models.IntegerField(blank=True, null=True)
    fesonetpatherrsecs = models.IntegerField(blank=True, null=True)
    fesonetpathseverrsecs = models.IntegerField(blank=True, null=True)
    fesonetpathunavailablesecs = models.IntegerField(blank=True, null=True)
    fesonetpathfc = models.IntegerField(blank=True, null=True)
    stspathwidth = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_sonet_path_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SonetSecPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    severrframesecs = models.IntegerField(blank=True, null=True)
    codeviolations = models.IntegerField(blank=True, null=True)
    errsecs = models.IntegerField(blank=True, null=True)
    severrsecs = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_sonet_sec_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SonetVtPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    sonetvtcodeviolations = models.IntegerField(blank=True, null=True)
    sonetvterrsecs = models.IntegerField(blank=True, null=True)
    sonetvtseverrsecs = models.IntegerField(blank=True, null=True)
    sonetlineunavailablesecs = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    fesonetvtcodeviolations = models.IntegerField(blank=True, null=True)
    fesonetvterrsecs = models.IntegerField(blank=True, null=True)
    fesonetvtseverrsecs = models.IntegerField(blank=True, null=True)
    fesonetlineunavailablesecs = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    vttype = models.NullBooleanField()
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454_sonet_vt_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454UserTable(models.Model):
    nedbaccessid = models.IntegerField()
    userid = models.CharField(max_length=64)
    privilegeid = models.ForeignKey(Ons15454PrivilegeTable, db_column='privilegeid', blank=True, null=True)
    lockout = models.NullBooleanField()
    lastlogintime = models.DateField(blank=True, null=True)
    failedlogincount = models.IntegerField(blank=True, null=True)
    disabled = models.NullBooleanField()
    changepwdnxtlogin = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ons15454_user_table'
        unique_together = (('nedbaccessid', 'userid'),)


class Ons15454SdhE1PmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.BigIntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    cvl = models.IntegerField(blank=True, null=True)
    esl = models.IntegerField(blank=True, null=True)
    sesl = models.IntegerField(blank=True, null=True)
    lossl = models.IntegerField(blank=True, null=True)
    rxpeb = models.IntegerField(blank=True, null=True)
    rxpbbe = models.IntegerField(blank=True, null=True)
    rxpes = models.IntegerField(blank=True, null=True)
    rxpses = models.IntegerField(blank=True, null=True)
    rxpuas = models.IntegerField(blank=True, null=True)
    rxpesr = models.IntegerField(blank=True, null=True)
    rxpsesr = models.IntegerField(blank=True, null=True)
    rxpbber = models.IntegerField(blank=True, null=True)
    txaiss = models.IntegerField(blank=True, null=True)
    txpeb = models.IntegerField(blank=True, null=True)
    txpbbe = models.IntegerField(blank=True, null=True)
    txpes = models.IntegerField(blank=True, null=True)
    txpses = models.IntegerField(blank=True, null=True)
    txpuas = models.IntegerField(blank=True, null=True)
    txpesr = models.IntegerField(blank=True, null=True)
    txpsesr = models.IntegerField(blank=True, null=True)
    txpbber = models.IntegerField(blank=True, null=True)
    rxaiss = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    ferxpeb = models.IntegerField(blank=True, null=True)
    ferxpes = models.IntegerField(blank=True, null=True)
    ferxpses = models.IntegerField(blank=True, null=True)
    ferxpbbe = models.IntegerField(blank=True, null=True)
    ferxpuas = models.IntegerField(blank=True, null=True)
    ferxpesr = models.IntegerField(blank=True, null=True)
    ferxpsesr = models.IntegerField(blank=True, null=True)
    ferxpbber = models.IntegerField(blank=True, null=True)
    fetxpeb = models.IntegerField(blank=True, null=True)
    fetxpes = models.IntegerField(blank=True, null=True)
    fetxpses = models.IntegerField(blank=True, null=True)
    fetxpbbe = models.IntegerField(blank=True, null=True)
    fetxpuas = models.IntegerField(blank=True, null=True)
    fetxpesr = models.IntegerField(blank=True, null=True)
    fetxpsesr = models.IntegerField(blank=True, null=True)
    fetxpbber = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454sdh_e1_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SdhE3PmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    cvl = models.IntegerField(blank=True, null=True)
    esl = models.IntegerField(blank=True, null=True)
    sesl = models.IntegerField(blank=True, null=True)
    lossl = models.IntegerField(blank=True, null=True)
    rxpes = models.IntegerField(blank=True, null=True)
    rxpses = models.IntegerField(blank=True, null=True)
    rxpuas = models.IntegerField(blank=True, null=True)
    rxpesr = models.IntegerField(blank=True, null=True)
    rxpsesr = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)
    txpes = models.IntegerField(blank=True, null=True)
    txpses = models.IntegerField(blank=True, null=True)
    txpuas = models.IntegerField(blank=True, null=True)
    txpesr = models.IntegerField(blank=True, null=True)
    txpsesr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454sdh_e3_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SdhE4PmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    codeviolations = models.IntegerField(blank=True, null=True)
    errsecs = models.IntegerField(blank=True, null=True)
    severrsecs = models.IntegerField(blank=True, null=True)
    unavailablesecs = models.IntegerField(blank=True, null=True)
    backgroundblockerrors = models.IntegerField(blank=True, null=True)
    esr = models.IntegerField(blank=True, null=True)
    sesr = models.IntegerField(blank=True, null=True)
    bber = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454sdh_e4_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SdhHoPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    hpeb = models.IntegerField(blank=True, null=True)
    hpes = models.IntegerField(blank=True, null=True)
    hpses = models.IntegerField(blank=True, null=True)
    hpuas = models.IntegerField(blank=True, null=True)
    hpbbe = models.IntegerField(blank=True, null=True)
    hpesr = models.IntegerField(blank=True, null=True)
    hpsesr = models.IntegerField(blank=True, null=True)
    hpbber = models.IntegerField(blank=True, null=True)
    hpppjcpdet = models.IntegerField(blank=True, null=True)
    hpnpjcpdet = models.IntegerField(blank=True, null=True)
    hpppjcpgen = models.IntegerField(blank=True, null=True)
    hpnpjcpgen = models.IntegerField(blank=True, null=True)
    hppjdiff = models.IntegerField(blank=True, null=True)
    hppjpsec = models.IntegerField(blank=True, null=True)
    hppjnsec = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    fehpeb = models.IntegerField(blank=True, null=True)
    fehpes = models.IntegerField(blank=True, null=True)
    fehpses = models.IntegerField(blank=True, null=True)
    fehpuas = models.IntegerField(blank=True, null=True)
    fehpbbe = models.IntegerField(blank=True, null=True)
    fehpesr = models.IntegerField(blank=True, null=True)
    fehpsesr = models.IntegerField(blank=True, null=True)
    fehpbber = models.IntegerField(blank=True, null=True)
    stspathwidth = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    hpfc = models.BigIntegerField(blank=True, null=True)
    fehpfc = models.BigIntegerField(blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454sdh_ho_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SdhLoPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    lotype = models.NullBooleanField()
    loeb = models.IntegerField(blank=True, null=True)
    lobbe = models.IntegerField(blank=True, null=True)
    loes = models.IntegerField(blank=True, null=True)
    loses = models.IntegerField(blank=True, null=True)
    louas = models.IntegerField(blank=True, null=True)
    loesr = models.IntegerField(blank=True, null=True)
    losesr = models.IntegerField(blank=True, null=True)
    lobber = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    feloeb = models.IntegerField(blank=True, null=True)
    felobbe = models.IntegerField(blank=True, null=True)
    feloes = models.IntegerField(blank=True, null=True)
    feloses = models.IntegerField(blank=True, null=True)
    felouas = models.IntegerField(blank=True, null=True)
    feloesr = models.IntegerField(blank=True, null=True)
    felosesr = models.IntegerField(blank=True, null=True)
    felobber = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454sdh_lo_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SdhMsPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    mseb = models.IntegerField(blank=True, null=True)
    mses = models.IntegerField(blank=True, null=True)
    msses = models.IntegerField(blank=True, null=True)
    msuas = models.IntegerField(blank=True, null=True)
    msppjcpdet = models.IntegerField(blank=True, null=True)
    msnpjcpdet = models.IntegerField(blank=True, null=True)
    msppjcpgen = models.IntegerField(blank=True, null=True)
    msnpjcpgen = models.IntegerField(blank=True, null=True)
    mspsc = models.IntegerField(blank=True, null=True)
    mspsd = models.IntegerField(blank=True, null=True)
    mspscw = models.IntegerField(blank=True, null=True)
    mspsdw = models.IntegerField(blank=True, null=True)
    mspscs = models.IntegerField(blank=True, null=True)
    mspsds = models.IntegerField(blank=True, null=True)
    mspscr = models.IntegerField(blank=True, null=True)
    mspsdr = models.IntegerField(blank=True, null=True)
    msbbe = models.IntegerField(blank=True, null=True)
    mspscmspsd = models.IntegerField(blank=True, null=True)
    msfc = models.IntegerField(blank=True, null=True)
    msesr = models.IntegerField(blank=True, null=True)
    mssesr = models.IntegerField(blank=True, null=True)
    msbber = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    femseb = models.IntegerField(blank=True, null=True)
    femses = models.IntegerField(blank=True, null=True)
    femsses = models.IntegerField(blank=True, null=True)
    femsuas = models.IntegerField(blank=True, null=True)
    femsbbe = models.IntegerField(blank=True, null=True)
    femsesr = models.IntegerField(blank=True, null=True)
    femssesr = models.IntegerField(blank=True, null=True)
    femsbber = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    femsfc = models.BigIntegerField(blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454sdh_ms_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15454SdhRsPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    rseb = models.IntegerField(blank=True, null=True)
    rses = models.IntegerField(blank=True, null=True)
    rsses = models.IntegerField(blank=True, null=True)
    rsbbe = models.IntegerField(blank=True, null=True)
    rssefs = models.IntegerField(blank=True, null=True)
    rsesr = models.IntegerField(blank=True, null=True)
    rssesr = models.IntegerField(blank=True, null=True)
    rsbber = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    rsofs = models.IntegerField(blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15454sdh_rs_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15501NeExplorerTable(models.Model):
    nedbaccessid = models.IntegerField(primary_key=True)
    timestamp = models.DateField()
    inputopticalpower = models.IntegerField(blank=True, null=True)
    inputopticalpowermean = models.IntegerField(blank=True, null=True)
    inputopticalpowertrigger = models.IntegerField(blank=True, null=True)
    outputopticalpower = models.IntegerField(blank=True, null=True)
    outputopticalsignalpower = models.IntegerField(blank=True, null=True)
    outputopticalsignalpowermean = models.IntegerField(blank=True, null=True)
    outputopticalsignalpwrtrigger = models.IntegerField(blank=True, null=True)
    opticalpowergain = models.IntegerField(blank=True, null=True)
    meanopticalpowergain = models.IntegerField(blank=True, null=True)
    gaintrigger = models.IntegerField(blank=True, null=True)
    ambienttemp = models.IntegerField(blank=True, null=True)
    ambienttempmean = models.IntegerField(blank=True, null=True)
    ambienttemptrigger = models.IntegerField(blank=True, null=True)
    powersupply1level = models.IntegerField(blank=True, null=True)
    powersupply2level = models.IntegerField(blank=True, null=True)
    powersupply1status = models.CharField(max_length=20, blank=True, null=True)
    powersupply2status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15501_ne_explorer_table'


class Ons15501OptPowerPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    interval = models.BooleanField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    thresholdmask = models.BigIntegerField(blank=True, null=True)
    inputopticalpower = models.IntegerField(blank=True, null=True)
    outputopticalpower = models.IntegerField(blank=True, null=True)
    outputopticalsignalpower = models.IntegerField(blank=True, null=True)
    opticalpowergain = models.IntegerField(blank=True, null=True)
    ambienttemp = models.IntegerField(blank=True, null=True)
    powersupply1level = models.IntegerField(blank=True, null=True)
    powersupply2level = models.IntegerField(blank=True, null=True)
    modeltype = models.IntegerField()
    objecttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons15501_opt_power_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'modeltype', 'objecttype', 'interval'),)


class Ons155XxCdlFlowConfig(models.Model):
    ifdbaccessid = models.ForeignKey(Mib2InterfaceTable, db_column='ifdbaccessid', primary_key=True)
    nedbaccessid = models.IntegerField()
    cdlxmitflowid = models.IntegerField(blank=True, null=True)
    cdlrcvflowid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_cdl_flow_config'


class Ons155XxCdlIfConfig(models.Model):
    ifdbaccessid = models.ForeignKey(Mib2InterfaceTable, db_column='ifdbaccessid', primary_key=True)
    nedbaccessid = models.IntegerField()
    cdladminstatus = models.IntegerField(blank=True, null=True)
    cdlforceendofhop = models.IntegerField(blank=True, null=True)
    cdlnodebehavior = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_cdl_if_config'


class Ons155XxCdlPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    interval = models.BooleanField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    thresholdmask = models.BigIntegerField(blank=True, null=True)
    rxhec = models.BigIntegerField(blank=True, null=True)
    rxnoncdl = models.BigIntegerField(blank=True, null=True)
    rxinvalidflowid = models.BigIntegerField(blank=True, null=True)
    netethernetcrc = models.BigIntegerField(blank=True, null=True)
    modeltype = models.IntegerField()
    objecttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons155xx_cdl_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'modeltype', 'objecttype', 'interval'),)


class Ons155XxCircuitCcTbl(models.Model):
    cktccdbid = models.IntegerField(primary_key=True)
    cktnodeid = models.ForeignKey(CircuitTbl, db_column='cktnodeid')
    cktuniqueid = models.ForeignKey(CircuitTbl, db_column='cktuniqueid')
    cktccnodeid = models.IntegerField()
    cktccsrcphysicalloc = models.BigIntegerField(blank=True, null=True)
    cktccsrcifindex = models.BigIntegerField(blank=True, null=True)
    cktccsrcmoduletype = models.IntegerField(blank=True, null=True)
    cktccsrcobjecttype = models.IntegerField(blank=True, null=True)
    cktccsrcmodeltype = models.IntegerField(blank=True, null=True)
    cktccdestphysicalloc = models.BigIntegerField(blank=True, null=True)
    cktccdestifindex = models.BigIntegerField(blank=True, null=True)
    cktccdestmoduletype = models.IntegerField(blank=True, null=True)
    cktccdestobjecttype = models.IntegerField(blank=True, null=True)
    cktccdestmodeltype = models.IntegerField(blank=True, null=True)
    cktccsrcwavelength = models.CharField(max_length=64, blank=True, null=True)
    cktccdestwavelength = models.CharField(max_length=64, blank=True, null=True)
    cktcctechnology = models.NullBooleanField()
    cktccsrcstate = models.NullBooleanField()
    cktccdeststate = models.NullBooleanField()
    iscktccworking = models.NullBooleanField()
    iscktccactive = models.NullBooleanField()
    cktccdescr = models.CharField(max_length=256, blank=True, null=True)
    cktccsrccdlflowid = models.IntegerField(blank=True, null=True)
    cktccdestcdlflowid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_circuit_cc_tbl'


class Ons155XxCircuitPathTbl(models.Model):
    cktnodeid = models.IntegerField()
    cktuniqueid = models.IntegerField()
    pathdbid = models.ForeignKey('Ons155XxPathTbl', db_column='pathdbid')
    pathseqnum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons155xx_circuit_path_tbl'
        unique_together = (('cktnodeid', 'cktuniqueid', 'pathdbid'),)


class Ons155XxCircuitStackTbl(models.Model):
    llcktnodeid = models.ForeignKey(CircuitTbl, db_column='llcktnodeid')
    llcktuniqueid = models.ForeignKey(CircuitTbl, db_column='llcktuniqueid')
    hlcktnodeid = models.ForeignKey(CircuitTbl, db_column='hlcktnodeid')
    hlcktuniqueid = models.ForeignKey(CircuitTbl, db_column='hlcktuniqueid')
    llcktpathdbid = models.ForeignKey('Ons155XxPathTbl', db_column='llcktpathdbid')
    hlcktpathdbid = models.ForeignKey('Ons155XxPathTbl', db_column='hlcktpathdbid')
    lltohlcktassoctype = models.NullBooleanField()
    lltohlcktassoctechinfo = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_circuit_stack_tbl'
        unique_together = (('llcktnodeid', 'llcktuniqueid', 'hlcktnodeid', 'hlcktuniqueid', 'llcktpathdbid', 'hlcktpathdbid'),)


class Ons155XxCondtypeMap(models.Model):
    nemodeltype = models.IntegerField()
    descrid = models.CharField(max_length=255)
    condtype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons155xx_condtype_map'
        unique_together = (('nemodeltype', 'descrid'),)


class Ons155XxDcrpDefinitionTable(models.Model):
    dcrptypedbid = models.IntegerField(primary_key=True)
    dcrpname = models.CharField(max_length=64)
    dcrpseverity = models.NullBooleanField()
    dcrpprobcause = models.CharField(max_length=256, blank=True, null=True)
    dcrprecaction = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_dcrp_definition_table'


class Ons155XxDcrpTable(models.Model):
    dcrpdbid = models.IntegerField(primary_key=True)
    dcrptypedbid = models.ForeignKey(Ons155XxDcrpDefinitionTable, db_column='dcrptypedbid')
    dcrpidentifier = models.CharField(max_length=64, blank=True, null=True)
    nedbaccessid1 = models.IntegerField(blank=True, null=True)
    nedbaccessid2 = models.IntegerField(blank=True, null=True)
    dcrptimestamp = models.DateField(blank=True, null=True)
    dcrpdescr = models.CharField(max_length=256, blank=True, null=True)
    dcrpdetails = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_dcrp_table'


class Ons155XxDiscoveryInfoTable(models.Model):
    nedbaccessid = models.IntegerField(primary_key=True)
    starttime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    status = models.BooleanField()
    startmode = models.BooleanField()
    descr = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_discovery_info_table'


class Ons155XxEtherHistPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    interval = models.BooleanField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    thresholdmask = models.BigIntegerField(blank=True, null=True)
    octets = models.BigIntegerField(blank=True, null=True)
    pkts = models.BigIntegerField(blank=True, null=True)
    crcalignerrors = models.BigIntegerField(blank=True, null=True)
    undersizepkts = models.BigIntegerField(blank=True, null=True)
    oversizepkts = models.BigIntegerField(blank=True, null=True)
    modeltype = models.IntegerField()
    objecttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons155xx_ether_hist_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'modeltype', 'objecttype', 'interval'),)


class Ons155XxFcmPePmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    interval = models.BooleanField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    thresholdmask = models.BigIntegerField(blank=True, null=True)
    rxlinkresets = models.BigIntegerField(blank=True, null=True)
    txlinkresets = models.BigIntegerField(blank=True, null=True)
    linkresets = models.BigIntegerField(blank=True, null=True)
    rxofflinesequences = models.BigIntegerField(blank=True, null=True)
    txofflinesequences = models.BigIntegerField(blank=True, null=True)
    linkfailures = models.BigIntegerField(blank=True, null=True)
    lossofsynchs = models.BigIntegerField(blank=True, null=True)
    lossofsignals = models.BigIntegerField(blank=True, null=True)
    primseqprotocolerrors = models.BigIntegerField(blank=True, null=True)
    invalidtxwords = models.BigIntegerField(blank=True, null=True)
    invalidcrcs = models.BigIntegerField(blank=True, null=True)
    invalidorderedsets = models.BigIntegerField(blank=True, null=True)
    frametoolongs = models.BigIntegerField(blank=True, null=True)
    truncatedframes = models.BigIntegerField(blank=True, null=True)
    addresserrors = models.BigIntegerField(blank=True, null=True)
    delimitererrors = models.BigIntegerField(blank=True, null=True)
    encodingdisparityerrors = models.BigIntegerField(blank=True, null=True)
    othererrors = models.BigIntegerField(blank=True, null=True)
    modeltype = models.IntegerField()
    objecttype = models.IntegerField()
    ifinoctets = models.BigIntegerField(blank=True, null=True)
    ifinucastpkts = models.BigIntegerField(blank=True, null=True)
    ifoutoctets = models.BigIntegerField(blank=True, null=True)
    ifoutucastpkts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_fcm_pe_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'modeltype', 'objecttype', 'interval'),)


class Ons155XxFlashDeviceTable(models.Model):
    flashdevdbid = models.IntegerField(primary_key=True)
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    flashdevindex = models.IntegerField()
    flashdevname = models.CharField(max_length=16)
    flashdevsize = models.IntegerField(blank=True, null=True)
    flashdevpartitions = models.IntegerField(blank=True, null=True)
    cpuslotnum = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_flash_device_table'


class Ons155XxFlashPartitionTable(models.Model):
    flashpartdbid = models.IntegerField(primary_key=True)
    flashdevdbid = models.ForeignKey(Ons155XxFlashDeviceTable, db_column='flashdevdbid')
    flashpartindex = models.IntegerField()
    flashpartname = models.CharField(max_length=16)
    flashpartsize = models.IntegerField(blank=True, null=True)
    flashpartfreesize = models.IntegerField(blank=True, null=True)
    flashpartstatus = models.NullBooleanField()
    flashpartfilenamelen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_flash_partition_table'


class Ons155XxGraCcToCktCcTbl(models.Model):
    granularccdbid = models.ForeignKey('Ons155XxGranularCcTbl', db_column='granularccdbid')
    cktcrossconnectdbid = models.ForeignKey(Ons155XxCircuitCcTbl, db_column='cktcrossconnectdbid')
    granularccseqnum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_gra_cc_to_ckt_cc_tbl'
        unique_together = (('granularccdbid', 'cktcrossconnectdbid'),)


class Ons155XxGranularCcTbl(models.Model):
    gccdbid = models.IntegerField(primary_key=True)
    gccsrcnodeid = models.ForeignKey(NeInfoTable, db_column='gccsrcnodeid')
    gccsrcphysicalloc = models.BigIntegerField(blank=True, null=True)
    gccsrcifindex = models.BigIntegerField(blank=True, null=True)
    gccsrcmoduletype = models.IntegerField(blank=True, null=True)
    gccsrcobjecttype = models.IntegerField(blank=True, null=True)
    gccsrcmodeltype = models.IntegerField(blank=True, null=True)
    gccdestnodeid = models.ForeignKey(NeInfoTable, db_column='gccdestnodeid')
    gccdestphysicalloc = models.BigIntegerField(blank=True, null=True)
    gccdestifindex = models.BigIntegerField(blank=True, null=True)
    gccdestmoduletype = models.IntegerField(blank=True, null=True)
    gccdestobjecttype = models.IntegerField(blank=True, null=True)
    gccdestmodeltype = models.IntegerField(blank=True, null=True)
    gccprovisiontype = models.NullBooleanField()
    gcctechnology = models.NullBooleanField()
    gccprottype = models.NullBooleanField()
    gccsrctodestoperstatus = models.NullBooleanField()
    gccdesttosrcoperstatus = models.NullBooleanField()
    gccassoclinktype = models.NullBooleanField()
    gccassoclinkdbid = models.IntegerField(blank=True, null=True)
    gccdirectionaltype = models.NullBooleanField()
    gccdescr = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_granular_cc_tbl'


class Ons155XxIfCircuitParamsTbl(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    ifphysicalloc = models.BigIntegerField()
    ifindex = models.BigIntegerField()
    ifmoduletype = models.IntegerField()
    ifobjecttype = models.IntegerField()
    ifmodeltype = models.IntegerField()
    cktname = models.CharField(max_length=64)
    cktdescr = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'ons155xx_if_circuit_params_tbl'
        unique_together = (('nedbaccessid', 'ifphysicalloc', 'ifindex', 'ifmoduletype', 'ifobjecttype', 'ifmodeltype'),)


class Ons155XxIfOpticalPower(models.Model):
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid')
    pwrsrcphysicalloc = models.BigIntegerField()
    pwrsrcifindex = models.BigIntegerField()
    pwrsrcmoduletype = models.IntegerField()
    pwrsrcmodeltype = models.IntegerField()
    pwrsrcobjecttype = models.IntegerField()
    pwrmondirection = models.BooleanField()
    pwrmonlocation = models.BooleanField()
    opticalpower = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'ons155xx_if_optical_power'
        unique_together = (('nedbaccessid', 'pwrsrcphysicalloc', 'pwrsrcifindex', 'pwrsrcmoduletype', 'pwrsrcmodeltype', 'pwrsrcobjecttype', 'pwrmondirection', 'pwrmonlocation'),)


class Ons155XxIfPhyInfoTable(models.Model):
    ifdbaccessid = models.IntegerField(primary_key=True)
    nedbaccessid = models.IntegerField()
    ifmode = models.NullBooleanField()
    ifprotocol = models.IntegerField(blank=True, null=True)
    ifclockrate = models.IntegerField(blank=True, null=True)
    ifmonitor = models.NullBooleanField()
    ifloopback = models.NullBooleanField()
    ifofc = models.NullBooleanField()
    iflsc = models.NullBooleanField()
    ifflc = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ons155xx_if_phy_info_table'


class Ons155XxNeInfoTable(models.Model):
    nedbaccessid = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=64, blank=True, null=True)
    globalid = models.CharField(max_length=64, blank=True, null=True)
    sysobjectid = models.CharField(max_length=256, blank=True, null=True)
    syscontact = models.CharField(max_length=256, blank=True, null=True)
    syslocation = models.CharField(max_length=256, blank=True, null=True)
    sysdescr = models.CharField(max_length=256, blank=True, null=True)
    lastboottime = models.DateField(blank=True, null=True)
    lastswitchovertime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_ne_info_table'


class Ons155XxNeTypeTable(models.Model):
    modeltype = models.ForeignKey(ModelTypeTable, db_column='modeltype')
    sysobjectid = models.CharField(max_length=256)
    imageversion = models.CharField(max_length=64, blank=True, null=True)
    smffactory = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_ne_type_table'


class Ons155XxOptPowerPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    interval = models.BooleanField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    thresholdmask = models.BigIntegerField(blank=True, null=True)
    meanpower = models.IntegerField(blank=True, null=True)
    maxpower = models.IntegerField(blank=True, null=True)
    minpower = models.IntegerField(blank=True, null=True)
    meanambtemp = models.IntegerField(blank=True, null=True)
    maxambtemp = models.IntegerField(blank=True, null=True)
    minambtemp = models.IntegerField(blank=True, null=True)
    meanlasertemp = models.IntegerField(blank=True, null=True)
    maxlasertemp = models.IntegerField(blank=True, null=True)
    minlasertemp = models.IntegerField(blank=True, null=True)
    meanbiascurrent = models.IntegerField(blank=True, null=True)
    maxbiascurrent = models.IntegerField(blank=True, null=True)
    minbiascurrent = models.IntegerField(blank=True, null=True)
    availablesecs = models.IntegerField(blank=True, null=True)
    direction = models.BooleanField()
    location = models.BooleanField()
    modeltype = models.IntegerField()
    objecttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons155xx_opt_power_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'modeltype', 'objecttype', 'interval', 'direction', 'location'),)


class Ons155XxPathHopTbl(models.Model):
    pathdbid = models.ForeignKey('Ons155XxPathTbl', db_column='pathdbid')
    pathhopid = models.IntegerField()
    pathhoptype = models.BooleanField()
    pathhopdbid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons155xx_path_hop_tbl'
        unique_together = (('pathdbid', 'pathhoptype', 'pathhopdbid'),)


class Ons155XxPathTbl(models.Model):
    pathdbid = models.IntegerField(primary_key=True)
    pathsrcnodeid = models.ForeignKey(NeInfoTable, db_column='pathsrcnodeid')
    pathsrcphysicalloc = models.BigIntegerField(blank=True, null=True)
    pathsrcifindex = models.BigIntegerField(blank=True, null=True)
    pathsrcmoduletype = models.IntegerField(blank=True, null=True)
    pathsrcobjecttype = models.IntegerField(blank=True, null=True)
    pathsrcmodeltype = models.IntegerField(blank=True, null=True)
    pathdestnodeid = models.ForeignKey(NeInfoTable, db_column='pathdestnodeid')
    pathdestphysicalloc = models.BigIntegerField(blank=True, null=True)
    pathdestifindex = models.BigIntegerField(blank=True, null=True)
    pathdestmoduletype = models.IntegerField(blank=True, null=True)
    pathdestobjecttype = models.IntegerField(blank=True, null=True)
    pathdestmodeltype = models.IntegerField(blank=True, null=True)
    pathstatus = models.NullBooleanField()
    isworking = models.NullBooleanField()
    isactive = models.NullBooleanField()
    downinterfaces = models.CharField(max_length=256, blank=True, null=True)
    pathdescr = models.CharField(max_length=256, blank=True, null=True)
    pathdestpwrmonnodeid = models.IntegerField(blank=True, null=True)
    pathdestpwrmonphysicalloc = models.BigIntegerField(blank=True, null=True)
    pathdestpwrmonifindex = models.BigIntegerField(blank=True, null=True)
    pathdestpwrmonmoduletype = models.IntegerField(blank=True, null=True)
    pathdestpwrmonobjecttype = models.IntegerField(blank=True, null=True)
    pathdestpwrmonmodeltype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons155xx_path_tbl'


class Ons155XxPhyPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    interval = models.BooleanField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    thresholdmask = models.BigIntegerField(blank=True, null=True)
    rxcvrd = models.BigIntegerField(blank=True, null=True)
    rxcrc = models.BigIntegerField(blank=True, null=True)
    txencapfarendpkterrors = models.BigIntegerField(blank=True, null=True)
    modeltype = models.IntegerField()
    objecttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons155xx_phy_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'modeltype', 'objecttype', 'interval'),)


class Ons155XxSonetSecPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    interval = models.BooleanField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    thresholdmask = models.BigIntegerField(blank=True, null=True)
    severrsecs = models.IntegerField(blank=True, null=True)
    severrframingsecs = models.IntegerField(blank=True, null=True)
    errsecs = models.IntegerField(blank=True, null=True)
    codeviolations = models.BigIntegerField(blank=True, null=True)
    modeltype = models.IntegerField()
    objecttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ons155xx_sonet_sec_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'modeltype', 'objecttype', 'interval'),)


class Ons15600EnetPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    ifinoctets = models.BigIntegerField(blank=True, null=True)
    ifinucastpkts = models.BigIntegerField(blank=True, null=True)
    ifinmulticastpkts = models.BigIntegerField(blank=True, null=True)
    ifinbroadcastpkts = models.BigIntegerField(blank=True, null=True)
    ifindiscards = models.BigIntegerField(blank=True, null=True)
    ifinerrors = models.BigIntegerField(blank=True, null=True)
    ifoutoctets = models.BigIntegerField(blank=True, null=True)
    ifoutucastpkts = models.BigIntegerField(blank=True, null=True)
    ifoutmulticastpkts = models.BigIntegerField(blank=True, null=True)
    ifoutbroadcastpkts = models.BigIntegerField(blank=True, null=True)
    ifoutdiscards = models.BigIntegerField(blank=True, null=True)
    dot3statsalignmenterrors = models.BigIntegerField(blank=True, null=True)
    dot3statsfcserrors = models.BigIntegerField(blank=True, null=True)
    dot3statsframetoolong = models.BigIntegerField(blank=True, null=True)
    etherstatsundersizepkts = models.BigIntegerField(blank=True, null=True)
    etherstatsfragments = models.BigIntegerField(blank=True, null=True)
    etherstatspkts64octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts65to127octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts128to255octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts256to511octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts512to1023octets = models.BigIntegerField(blank=True, null=True)
    etherstatspkts1024to1518octets = models.BigIntegerField(blank=True, null=True)
    etherstatsbroadcastpkts = models.BigIntegerField(blank=True, null=True)
    etherstatsmulticastpkts = models.BigIntegerField(blank=True, null=True)
    etherstatsoversizepkts = models.BigIntegerField(blank=True, null=True)
    etherstatsjabbers = models.BigIntegerField(blank=True, null=True)
    etherstatsoctets = models.BigIntegerField(blank=True, null=True)
    etherstatsdropevents = models.BigIntegerField(blank=True, null=True)
    rxpauseframes = models.BigIntegerField(blank=True, null=True)
    txpauseframes = models.BigIntegerField(blank=True, null=True)
    etherstatspkts = models.BigIntegerField(blank=True, null=True)
    ifouterrors = models.BigIntegerField(blank=True, null=True)
    dot3statsinternalmacrxerrors = models.BigIntegerField(blank=True, null=True)
    dot3statsinternalmactxerrors = models.BigIntegerField(blank=True, null=True)
    dot3statssymbolerrors = models.BigIntegerField(blank=True, null=True)
    rxetherutilizationstats = models.IntegerField(blank=True, null=True)
    txetherutilizationstats = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15600_enet_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Ons15600PosPmTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduletype = models.IntegerField()
    physicalloc = models.BigIntegerField()
    neifindex = models.BigIntegerField()
    timestamp = models.DateField()
    neifpmstatus = models.BigIntegerField()
    inmaintenance = models.NullBooleanField()
    fifteenminthresholdmask = models.IntegerField(blank=True, null=True)
    thresholdlist = models.CharField(max_length=1024, blank=True, null=True)
    hdlcinoctets = models.BigIntegerField(blank=True, null=True)
    hdlcoutoctets = models.BigIntegerField(blank=True, null=True)
    rxtotalpackets = models.BigIntegerField(blank=True, null=True)
    txtotalpackets = models.BigIntegerField(blank=True, null=True)
    hdlcrxaborts = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframesbadcrc = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxframe = models.BigIntegerField(blank=True, null=True)
    gfpstatstxframe = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxoctets = models.BigIntegerField(blank=True, null=True)
    gfpstatstxoctets = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxcrcerrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxmbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxsbiterrors = models.BigIntegerField(blank=True, null=True)
    gfpstatsrxtypeinvalid = models.BigIntegerField(blank=True, null=True)
    rxpktsdroppedinernalcongestion = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxshortpkts = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframestruncated = models.BigIntegerField(blank=True, null=True)
    mediaindstatsrxframestoolong = models.BigIntegerField(blank=True, null=True)
    rxetherutilizationstats = models.IntegerField(blank=True, null=True)
    txetherutilizationstats = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)
    invaliditylist = models.CharField(max_length=1024, blank=True, null=True)
    strcorbatidaid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ons15600_pos_pm_table'
        unique_together = (('nedbaccessid', 'timestamp', 'moduletype', 'physicalloc', 'neifindex', 'is24h', 'neifpmstatus'),)


class Opaqueidtable(models.Model):
    id = models.ForeignKey('TerminationPointTable', db_column='id', primary_key=True)
    opaqueid = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opaqueidtable'


class OperationPermissionsTable(models.Model):
    usertypeid = models.ForeignKey('UserTypeTable', db_column='usertypeid')
    operationid = models.ForeignKey('OperationsTable', db_column='operationid')
    permission = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'operation_permissions_table'
        unique_together = (('usertypeid', 'operationid'),)


class OperationsTable(models.Model):
    operationid = models.IntegerField(primary_key=True)
    operationname = models.CharField(max_length=65)
    category = models.CharField(max_length=65, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    allowedpermissions = models.NullBooleanField()
    warning = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operations_table'


class OpticalsideTable(models.Model):
    name = models.CharField(max_length=765, blank=True, null=True)
    namenum = models.IntegerField(blank=True, null=True)
    osc = models.ForeignKey('TerminationPointTable', db_column='osc', blank=True, null=True)
    modelname = models.CharField(unique=True, max_length=765, blank=True, null=True)
    neid = models.ForeignKey(NeInfoTable, db_column='neid', blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    line_in = models.ForeignKey('TerminationPointTable', db_column='line_in', unique=True)
    line_out = models.ForeignKey('TerminationPointTable', db_column='line_out', unique=True)

    class Meta:
        managed = False
        db_table = 'opticalside_table'


class OrderConfigColumn(models.Model):
    viewid = models.ForeignKey(CustomViewConfig, db_column='viewid')
    order_attr = models.CharField(max_length=765, blank=True, null=True)
    order_direction = models.CharField(max_length=765, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_config_column'
        unique_together = (('viewid', 'position'),)


class OssActiveUserTable(models.Model):
    sessionid = models.IntegerField(primary_key=True)
    ossname = models.ForeignKey('OssUserTable', db_column='ossname')
    ipaddress = models.IntegerField()
    timeofconection = models.DateField(blank=True, null=True)
    listenermodeflag = models.NullBooleanField()
    domainmgrflag = models.NullBooleanField()
    ipv6addr = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_ipv6 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'oss_active_user_table'


class OssAidEnumTable(models.Model):
    aidid = models.IntegerField(primary_key=True)
    aidstring = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'oss_aid_enum_table'


class OssAlarmFilterTable(models.Model):
    alarmfilterid = models.IntegerField(primary_key=True)
    filtername = models.CharField(unique=True, max_length=128)
    alarmseverity = models.NullBooleanField()
    eventreportingflag = models.NullBooleanField()
    alarmreportingflag = models.NullBooleanField()
    pmreportingflag = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'oss_alarm_filter_table'


class OssAlarmFltrAidDenyTbl(models.Model):
    alarmfilterid = models.IntegerField()
    aidid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oss_alarm_fltr_aid_deny_tbl'
        unique_together = (('alarmfilterid', 'aidid'),)


class OssAlarmFltrTidDenyTbl(models.Model):
    alarmfilterid = models.IntegerField()
    nedbaccessid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oss_alarm_fltr_tid_deny_tbl'
        unique_together = (('alarmfilterid', 'nedbaccessid'),)


class OssCorbaUserTable(models.Model):
    ipaddress = models.IntegerField(blank=True, null=True)
    ossname = models.CharField(unique=True, max_length=128)
    osspasswd = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oss_corba_user_table'


class OssUserTable(models.Model):
    ipaddress = models.IntegerField(blank=True, null=True)
    ossname = models.CharField(unique=True, max_length=128)
    osspasswd = models.CharField(max_length=128)
    listenermodeflag = models.NullBooleanField()
    actuserdenyflag = models.NullBooleanField()
    alarmfilterflag = models.NullBooleanField()
    alarmfilterid = models.IntegerField(blank=True, null=True)
    domainmgrflag = models.NullBooleanField()
    ipv6addr = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_ipv6 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'oss_user_table'


class PasswordHistoryTable(models.Model):
    userid = models.IntegerField()
    userpassword = models.TextField(blank=True, null=True)  # This field type is a guess.
    timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_history_table'


class PatchcordTable(models.Model):
    linkid = models.IntegerField(primary_key=True)
    virtuallinkidsrc = models.IntegerField(blank=True, null=True)
    virtuallinkiddst = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patchcord_table'


class PmAttrValueMappingTable(models.Model):
    pmviewname = models.CharField(max_length=64)
    attrindex = models.IntegerField()
    attrvalue = models.CharField(max_length=64)
    displaytext = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pm_attr_value_mapping_table'


class PmAttridMappingTable(models.Model):
    pmviewname = models.CharField(max_length=64)
    pmname = models.CharField(max_length=256)
    metadataindex = models.IntegerField()
    attrindex = models.IntegerField()
    validity_attrindex = models.IntegerField(blank=True, null=True)
    is24h = models.BooleanField()
    displaytext = models.CharField(max_length=64, blank=True, null=True)
    pmparamid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pm_attrid_mapping_table'


class PmCategoryViewTable(models.Model):
    modeltype = models.IntegerField()
    categoryviewname = models.CharField(max_length=256)
    nemodelviewname = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pm_category_view_table'
        unique_together = (('modeltype', 'categoryviewname'),)


class PmCerentInfoTable(models.Model):
    pmparamid = models.IntegerField(primary_key=True)
    pmtablename = models.CharField(max_length=256)
    pmtableparam = models.CharField(max_length=256)
    pmtablecolno = models.IntegerField(blank=True, null=True)
    dbcoltype = models.CharField(max_length=64, blank=True, null=True)
    dbcolsize = models.IntegerField(blank=True, null=True)
    tmfname = models.CharField(max_length=64, blank=True, null=True)
    location = models.CharField(max_length=4, blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    objecttypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pm_cerent_info_table'


class PmHistoricalAppointments(models.Model):
    nedbaccessid = models.IntegerField()
    intervaltype = models.BooleanField()
    originalscheduledtime = models.DateField()
    status = models.BooleanField()
    timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'pm_historical_appointments'
        unique_together = (('nedbaccessid', 'intervaltype', 'originalscheduledtime'),)


class PmMetadataInfoTable(models.Model):
    nemodel = models.IntegerField()
    nemodelindex = models.IntegerField()
    moduletype = models.IntegerField()
    interfacetype = models.CharField(max_length=64)
    basenemodelindex = models.IntegerField()
    basemoduletype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pm_metadata_info_table'
        unique_together = (('nemodelindex', 'moduletype', 'interfacetype'),)


class PmMetadataTable(models.Model):
    nemodel = models.IntegerField()
    nemodelindex = models.IntegerField()
    moduletype = models.IntegerField()
    pmcategory = models.CharField(max_length=64)
    objecttypeid = models.IntegerField()
    pmtablecolno = models.IntegerField()
    pmparamid = models.ForeignKey(PmCerentInfoTable, db_column='pmparamid')
    interfacetype = models.CharField(max_length=64)
    paramposition = models.IntegerField()
    validityposition = models.IntegerField()
    tcanumber = models.IntegerField()
    tcalocation = models.CharField(max_length=10, blank=True, null=True)
    direction = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pm_metadata_table'
        unique_together = (('nemodel', 'nemodelindex', 'moduletype', 'pmcategory', 'interfacetype', 'pmtablecolno', 'tcanumber'),)


class PmserviceAssociatedTabTable(models.Model):
    table_name = models.CharField(max_length=1000)
    service_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'pmservice_associated_tab_table'


class PortChannelMembersTable(models.Model):
    ne_node = models.ForeignKey('PortChannelTable')
    slot_number = models.ForeignKey('PortChannelTable', db_column='slot_number')
    port_channel = models.ForeignKey('PortChannelTable')
    eth_port_number = models.IntegerField()
    lacp_mode = models.NullBooleanField()
    lacp_port_priority = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'port_channel_members_table'
        unique_together = (('ne_node_id', 'slot_number', 'port_channel_id', 'eth_port_number'),)


class PortChannelTable(models.Model):
    ne_node = models.ForeignKey(NeInfoTable)
    slot_number = models.IntegerField()
    port_channel_id = models.IntegerField()
    admin_state = models.NullBooleanField()
    mtu = models.IntegerField(blank=True, null=True)
    hold_queue_in = models.IntegerField(blank=True, null=True)
    hold_queue_out = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'port_channel_table'
        unique_together = (('ne_node_id', 'slot_number', 'port_channel_id'),)


class ProtectiongroupTable(models.Model):
    name = models.CharField(max_length=765, blank=True, null=True)
    operation = models.CharField(max_length=765, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    modelname = models.CharField(unique=True, max_length=765, blank=True, null=True)
    neid = models.ForeignKey(NeInfoTable, db_column='neid', blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    protected_port = models.ForeignKey('TerminationPointTable', db_column='protected_port', unique=True)
    working_port = models.ForeignKey('TerminationPointTable', db_column='working_port', unique=True)

    class Meta:
        managed = False
        db_table = 'protectiongroup_table'


class ProxyServerTable(models.Model):
    neipaddr = models.CharField(max_length=64)
    gneipaddr = models.CharField(max_length=64)
    isproxyinggne = models.BooleanField()
    masklength = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)
    gneid = models.ForeignKey(GneTable, db_column='gneid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proxy_server_table'
        unique_together = (('neipaddr', 'gneipaddr'),)


class PurgedNeTable(models.Model):
    nedbaccessid = models.IntegerField()
    nesysid = models.CharField(max_length=128)
    neipaddress = models.IntegerField(blank=True, null=True)
    purgedtimestamp = models.DateField()
    status = models.BooleanField()
    purgecomment = models.CharField(max_length=512, blank=True, null=True)
    neipv6address = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_ipv6 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'purged_ne_table'


class PwEfp(models.Model):
    nedbid = models.ForeignKey(MplsServiceTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsServiceTable, db_column='ptsindex')
    serviceid = models.ForeignKey(MplsServiceTable, db_column='serviceid')
    serstate = models.BooleanField()
    isdoubletagged = models.BooleanField()
    isexact = models.BooleanField()
    isstatsenabled = models.BooleanField()
    portdirection = models.BooleanField()
    primaryloadbal = models.IntegerField()
    outvlantag = models.CharField(max_length=256)
    outvlantpid = models.IntegerField()
    invlantag = models.CharField(max_length=256)
    invlantpid = models.IntegerField()
    rwoutvlantag = models.CharField(max_length=256)
    rwoutvlantpid = models.IntegerField()
    rwinvlantag = models.CharField(max_length=256)
    rwinvlantpid = models.IntegerField()
    rwoperation = models.IntegerField()
    issymmetricenabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pw_efp'
        unique_together = (('nedbid', 'ptsindex', 'serviceid'),)


class PwEp(models.Model):
    nedbid = models.ForeignKey(MplsServiceTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsServiceTable, db_column='ptsindex')
    serviceid = models.ForeignKey(MplsServiceTable, db_column='serviceid')
    ctcindex = models.IntegerField()
    phyloc = models.BigIntegerField()
    ctmuniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    routeid = models.CharField(max_length=256)
    isprotected = models.BooleanField()
    enabledelay = models.IntegerField()
    isneverdisable = models.BooleanField()
    disabledelay = models.IntegerField()
    tinfotype = models.IntegerField()
    operstate = models.BooleanField()
    ifportindex = models.IntegerField()
    adminstate = models.BooleanField()
    rxbw = models.BigIntegerField()
    txbw = models.BigIntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)
    slotmoduletype = models.IntegerField()
    portmoduletype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pw_ep'
        unique_together = (('nedbid', 'ptsindex', 'serviceid'),)


class PwPp(models.Model):
    nedbid = models.ForeignKey(MplsServiceTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsServiceTable, db_column='ptsindex')
    serviceid = models.ForeignKey(MplsServiceTable, db_column='serviceid')
    workprot = models.IntegerField()
    ctcindex = models.IntegerField()
    phyloc = models.BigIntegerField()
    tunnelnum = models.IntegerField()
    ctmuniqid = models.IntegerField()
    linkid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    peerid = models.CharField(max_length=256)
    vcid = models.IntegerField()
    locallabel = models.IntegerField()
    remotelabel = models.IntegerField()
    pwclassname = models.CharField(max_length=256)
    slotmoduletype = models.IntegerField()
    portmoduletype = models.IntegerField()
    unmanagedpeer = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pw_pp'
        unique_together = (('nedbid', 'ptsindex', 'serviceid', 'ctcindex', 'tunnelnum'),)


class PwQos(models.Model):
    nedbid = models.ForeignKey(MplsServiceTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsServiceTable, db_column='ptsindex')
    serviceid = models.ForeignKey(MplsServiceTable, db_column='serviceid')
    tablemapname = models.CharField(max_length=256)
    ingressqospolicyname = models.CharField(max_length=256)
    egressqospolicyname = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'pw_qos'
        unique_together = (('nedbid', 'ptsindex', 'serviceid'),)


class PwSrv(models.Model):
    serviceid = models.IntegerField()
    ctmuniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    discoverystate = models.BooleanField()
    operstate = models.BooleanField()
    isprotected = models.BooleanField()
    epcount = models.IntegerField()
    pwtype = models.IntegerField()
    txbandwidth = models.BigIntegerField()
    rxbandwidth = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pw_srv'
        unique_together = (('serviceid', 'ctmuniqid'),)


class ReportColumn(models.Model):
    reportid = models.ForeignKey('Reportconfigurationentity', db_column='reportid')
    attr = models.CharField(max_length=765, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report_column'
        unique_together = (('reportid', 'position'),)


class Reportconfigurationentity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    autorefresh = models.BooleanField()
    customconfiguration = models.CharField(max_length=765, blank=True, null=True)
    defaultconfigurationname = models.CharField(max_length=765, blank=True, null=True)
    numberofrecordsperpage = models.IntegerField()
    refreshperiod = models.BigIntegerField()
    type = models.CharField(max_length=765, blank=True, null=True)
    customview = models.ForeignKey(CustomViewConfig, blank=True, null=True)
    user = models.ForeignKey('UserTable', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportconfigurationentity'


class RoleMappingTable(models.Model):
    userrole = models.BooleanField()
    usertypeid = models.ForeignKey('UserTypeTable', db_column='usertypeid')

    class Meta:
        managed = False
        db_table = 'role_mapping_table'
        unique_together = (('userrole', 'usertypeid'),)


class RollTable(models.Model):
    rollnodeid = models.IntegerField()
    connectionindex = models.IntegerField()
    rollfromcktnodeid = models.IntegerField()
    rollfromcktuniqueid = models.IntegerField()
    rolltocktnodeid = models.IntegerField(blank=True, null=True)
    rolltocktuniqueid = models.IntegerField(blank=True, null=True)
    rollstate = models.NullBooleanField()
    rollvalidsignal = models.NullBooleanField()
    rollmode = models.NullBooleanField()
    rollpathnodeid = models.IntegerField(blank=True, null=True)
    rollpathmoduletype = models.IntegerField(blank=True, null=True)
    rollpathifindex = models.BigIntegerField(blank=True, null=True)
    rollpathobjectindex = models.IntegerField(blank=True, null=True)
    rollpathphysicalloc = models.BigIntegerField(blank=True, null=True)
    rollpathmodeltype = models.IntegerField(blank=True, null=True)
    rollfromnodeid = models.IntegerField(blank=True, null=True)
    rollfrommoduletype = models.IntegerField(blank=True, null=True)
    rollfromifindex = models.BigIntegerField(blank=True, null=True)
    rollfromobjectindex = models.IntegerField(blank=True, null=True)
    rollfromphysicalloc = models.BigIntegerField(blank=True, null=True)
    rollfrommodeltype = models.IntegerField(blank=True, null=True)
    rolltonodeid = models.IntegerField(blank=True, null=True)
    rolltomoduletype = models.IntegerField(blank=True, null=True)
    rolltoifindex = models.BigIntegerField(blank=True, null=True)
    rolltoobjectindex = models.IntegerField(blank=True, null=True)
    rolltophysicalloc = models.BigIntegerField(blank=True, null=True)
    rolltomodeltype = models.IntegerField(blank=True, null=True)
    rollname = models.CharField(unique=True, max_length=128)
    canbecompleted = models.NullBooleanField()
    canbefinished = models.NullBooleanField()
    canbecancelled = models.NullBooleanField()
    canbeforced = models.NullBooleanField()
    rollfromcktsize = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roll_table'
        unique_together = (('rollnodeid', 'connectionindex', 'rollfromcktsize'),)


class RowidTemp(models.Model):
    myrowid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rowid_temp'


class ScheduleInfoTable(models.Model):
    activitytype = models.CharField(max_length=64)
    neservicename = models.CharField(max_length=256)
    runonmonday = models.BooleanField()
    runontuesday = models.BooleanField()
    runonwednesday = models.BooleanField()
    runonthursday = models.BooleanField()
    runonfriday = models.BooleanField()
    runonsaturday = models.BooleanField()
    runonsunday = models.BooleanField()
    activitystarttime = models.DateField()
    activityinterval = models.IntegerField()
    lastexecutiontime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule_info_table'
        unique_together = (('activitytype', 'neservicename'),)


class ServerMonitorTable(models.Model):
    parameterindex = models.ForeignKey('ServerParameterTable', db_column='parameterindex')
    value = models.CharField(max_length=32, blank=True, null=True)
    collectiontime = models.DateField(blank=True, null=True)
    nedbaccessid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_monitor_table'


class ServerParameterTable(models.Model):
    parameterindex = models.IntegerField(primary_key=True)
    parametername = models.CharField(max_length=32)
    displayname = models.CharField(max_length=64)
    modeltype = models.IntegerField()
    type = models.BooleanField()
    configproperty = models.CharField(max_length=32)
    objecttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_parameter_table'


class ServiceAvailabilityTable(models.Model):
    service_instance_name = models.CharField(max_length=256)
    status = models.BooleanField()
    first_activated = models.DateField()
    last_crash = models.DateField(blank=True, null=True)
    running_since = models.DateField(blank=True, null=True)
    past_uptime = models.BigIntegerField(blank=True, null=True)
    deactivated = models.DateField(blank=True, null=True)
    perc_uptime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_availability_table'


class Socks(models.Model):
    socksid = models.IntegerField(primary_key=True)
    port = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=765, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socks'


class SoftwareVersionTable(models.Model):
    modelindex = models.ForeignKey(ModelIndexTable, db_column='modelindex')
    modeltype = models.ForeignKey(ModelIndexTable, db_column='modeltype')
    softwareversion = models.CharField(max_length=128)
    factorydefault = models.CharField(max_length=10, blank=True, null=True)
    modelname = models.CharField(max_length=128, blank=True, null=True)
    elejar = models.CharField(max_length=128, blank=True, null=True)
    validationpattern = models.CharField(max_length=128, blank=True, null=True)
    apiversion = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software_version_table'
        unique_together = (('modelindex', 'modeltype', 'softwareversion'),)


class SubnetworkTable(models.Model):
    subnetid = models.IntegerField(primary_key=True)
    subnetname = models.CharField(unique=True, max_length=64, blank=True, null=True)
    subnetsystemtitle = models.CharField(max_length=64, blank=True, null=True)
    subnetuserlabel = models.CharField(max_length=64, blank=True, null=True)
    subnettype = models.NullBooleanField()
    subnettopology = models.IntegerField(blank=True, null=True)
    subnetgneid = models.IntegerField()
    npid = models.ForeignKey(NetworkPartitionTable, db_column='npid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subnetwork_table'


class SvcConfigTable(models.Model):
    sid = models.IntegerField(primary_key=True)
    svcname = models.CharField(max_length=64)
    nemodeltype = models.IntegerField()
    svckind = models.IntegerField()
    npid = models.IntegerField()
    necount = models.IntegerField()
    state = models.IntegerField()
    discoverymode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'svc_config_table'


class SvcInfoTable(models.Model):
    svcid = models.IntegerField(primary_key=True)
    svcname = models.CharField(max_length=64)
    svcpackageid = models.IntegerField()
    svckind = models.IntegerField()
    svcconfigname = models.CharField(max_length=64)
    isnpdependant = models.BooleanField()
    ior = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'svc_info_table'


class SvcNemodelTable(models.Model):
    svcclassname = models.CharField(max_length=64)
    svcnemodeltype = models.IntegerField()
    svcnetype = models.IntegerField()
    svckind = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'svc_nemodel_table'
        unique_together = (('svcclassname', 'svcnemodeltype'),)


class SvcPackageTable(models.Model):
    svcpackageid = models.IntegerField(primary_key=True)
    svcpackagename = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'svc_package_table'


class SvcPropertyTable(models.Model):
    sectionname = models.CharField(max_length=40, blank=True, null=True)
    propertyname = models.CharField(max_length=40, blank=True, null=True)
    activevalue = models.CharField(max_length=256, blank=True, null=True)
    sid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'svc_property_table'


class SwayUserPortTable(models.Model):
    userid = models.IntegerField()
    nedbaccessid = models.IntegerField()
    neportifindex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sway_user_port_table'
        unique_together = (('userid', 'nedbaccessid', 'neportifindex'),)


class SyslogFilterTable(models.Model):
    filter_id = models.IntegerField(blank=True, null=True)
    filter_type = models.CharField(max_length=50, blank=True, null=True)
    filter_facility = models.CharField(max_length=50, blank=True, null=True)
    filter_subfacility = models.CharField(max_length=50, blank=True, null=True)
    filter_severity = models.NullBooleanField()
    filter_mnemonic = models.CharField(max_length=50, blank=True, null=True)
    filter_description = models.CharField(max_length=250, blank=True, null=True)
    filter_wild_card = models.CharField(max_length=50, blank=True, null=True)
    subscription_id = models.CharField(max_length=50, blank=True, null=True)
    filter_device_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syslog_filter_table'


class SyslogMessageTable(models.Model):
    message_id = models.IntegerField(blank=True, null=True)
    ne_id = models.IntegerField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    facility = models.CharField(max_length=50, blank=True, null=True)
    subfacility = models.CharField(max_length=50, blank=True, null=True)
    severity = models.NullBooleanField()
    mnemonic = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syslog_message_table'


class TableInfo(models.Model):
    tablename = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'table_info'


class TcaEventTable(models.Model):
    nedbaccessid = models.IntegerField()
    moduleorifindex = models.BigIntegerField()
    alarmeventtype = models.IntegerField()
    moduletype = models.IntegerField(blank=True, null=True)
    physicalloc = models.BigIntegerField(blank=True, null=True)
    tcaeventtype = models.IntegerField()
    tcalocation = models.CharField(max_length=20, blank=True, null=True)
    tcaperiod = models.CharField(max_length=20, blank=True, null=True)
    tcavalue = models.CharField(max_length=20, blank=True, null=True)
    direction = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateField()
    neeventtimestamp = models.DateField()
    modeltype = models.IntegerField(blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    strobjinstance = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tca_event_table'


class TcaEventTypeTable(models.Model):
    ne_model_index = models.IntegerField()
    tca_number = models.IntegerField()
    tca_type = models.CharField(max_length=64, blank=True, null=True)
    tca_ctm_type = models.CharField(max_length=64, blank=True, null=True)
    tca_tmf_type = models.CharField(max_length=64, blank=True, null=True)
    tca_gwc_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tca_event_type_table'


class TeEp(models.Model):
    nedbid = models.ForeignKey(MplsServiceTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsServiceTable, db_column='ptsindex')
    serviceid = models.ForeignKey(MplsServiceTable, db_column='serviceid')
    phyloc = models.BigIntegerField()
    ctmuniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_ep'
        unique_together = (('nedbid', 'ptsindex', 'serviceid'),)


class TePp(models.Model):
    nedbid = models.ForeignKey(MplsServiceTable, db_column='nedbid')
    ptsindex = models.ForeignKey(MplsServiceTable, db_column='ptsindex')
    serviceid = models.ForeignKey(MplsServiceTable, db_column='serviceid')
    workprot = models.IntegerField()
    ctcindex = models.IntegerField()
    phyloc = models.BigIntegerField()
    tunnelnum = models.IntegerField()
    ctmuniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_pp'
        unique_together = (('nedbid', 'ptsindex', 'serviceid', 'ctcindex'),)


class TemplateDataTable(models.Model):
    variable_pkid = models.IntegerField(primary_key=True)
    fk_template_pkid = models.IntegerField()
    variable_name = models.CharField(max_length=128)
    variable_display_name = models.CharField(max_length=256)
    variable_type = models.BooleanField()
    range_choice_option = models.CharField(max_length=512, blank=True, null=True)
    default_value = models.CharField(max_length=256, blank=True, null=True)
    mandatory_flag = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'template_data_table'


class TemplateDatatypesTable(models.Model):
    enum = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=32)
    regex = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_datatypes_table'


class TemplateJobDataTable(models.Model):
    template_job_data_pkid = models.BigIntegerField(primary_key=True)
    fk_template_job_pkid = models.IntegerField()
    fk_variable_id = models.IntegerField()
    variable_value = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_job_data_table'


class TemplateJobTable(models.Model):
    template_job_pkid = models.IntegerField(primary_key=True)
    fk_ne_id = models.IntegerField()
    fk_ne_version = models.CharField(max_length=128, blank=True, null=True)
    fk_template_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'template_job_table'


class TemplateTable(models.Model):
    template_pkid = models.IntegerField(primary_key=True)
    template_name = models.CharField(unique=True, max_length=128)
    template_netype = models.CharField(max_length=128)
    template_neversion = models.CharField(max_length=128)
    template_data = models.TextField(blank=True, null=True)
    template_status_flag = models.BooleanField()
    template_description = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_table'


class TerminationPointTable(models.Model):
    adminstate = models.CharField(max_length=765)
    location = models.CharField(max_length=765, blank=True, null=True)
    opaque_id = models.CharField(max_length=765, blank=True, null=True)
    portname = models.CharField(max_length=765, blank=True, null=True)
    isactiveinprotection = models.NullBooleanField()
    role = models.CharField(max_length=765, blank=True, null=True)
    porttype = models.CharField(max_length=765, blank=True, null=True)
    servicestate = models.CharField(max_length=765, blank=True, null=True)
    payload = models.CharField(max_length=90, blank=True, null=True)
    side = models.CharField(max_length=765, blank=True, null=True)
    modelname = models.CharField(unique=True, max_length=765, blank=True, null=True)
    neid = models.ForeignKey(NeInfoTable, db_column='neid', blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    cardname = models.CharField(max_length=255, blank=True, null=True)
    wavelength = models.CharField(max_length=255, blank=True, null=True)
    max_link_layer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'termination_point_table'


class ThresholdTable(models.Model):
    thresholdtype = models.IntegerField()
    thresholdsubtype = models.IntegerField()
    thresholdstring = models.CharField(max_length=128, blank=True, null=True)
    fifteenminvalue = models.IntegerField()
    onedayvalue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'threshold_table'
        unique_together = (('thresholdtype', 'thresholdsubtype'),)


class Tl1EncodingTable(models.Model):
    enum = models.IntegerField(primary_key=True)
    encode_type = models.CharField(max_length=32)
    default_port = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tl1_encoding_table'


class Tl1TunnelGatewayTable(models.Model):
    ngne_pkid = models.IntegerField(primary_key=True)
    ngne_tid = models.CharField(max_length=128, blank=True, null=True)
    ngne_ipaddress = models.IntegerField()
    ngne_username = models.CharField(max_length=64, blank=True, null=True)
    ngne_user_password = models.CharField(max_length=64, blank=True, null=True)
    ngne_tl1port = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tl1_tunnel_gateway_table'


class Tl1TunnelInfoTable(models.Model):
    tunnel_pkid = models.IntegerField(primary_key=True)
    tne_ne_dbaccess_id = models.IntegerField(unique=True)
    fk_ngne_pkid = models.IntegerField(blank=True, null=True)
    tl1_encoding = models.IntegerField(blank=True, null=True)
    tl1_port_number = models.IntegerField(blank=True, null=True)
    tunnel_status = models.NullBooleanField()
    tunnel_description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tl1_tunnel_info_table'


class TmfThMappingTable(models.Model):
    th_id = models.IntegerField(blank=True, null=True)
    th_name = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmf_th_mapping_table'


class TopologyMap(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=765, blank=True, null=True)
    treenodetype = models.CharField(max_length=765, blank=True, null=True)
    group = models.ForeignKey(GroupInfoTable, blank=True, null=True)
    np = models.ForeignKey(NetworkPartitionTable, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topology_map'


class TpSrv(models.Model):
    serviceid = models.IntegerField()
    ctmuniqid = models.IntegerField()
    servicename = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    ctmworkinglspuniqid = models.IntegerField()
    ctmprotectlspuniqid = models.IntegerField()
    discoverystate = models.BooleanField()
    operstate = models.BooleanField()
    isprotected = models.BooleanField()
    wlspnum = models.IntegerField()
    plspnum = models.IntegerField()
    txbandwidth = models.BigIntegerField()
    rxbandwidth = models.BigIntegerField()
    tunkey = models.CharField(max_length=256, blank=True, null=True)
    epcount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tp_srv'
        unique_together = (('serviceid', 'ctmuniqid'),)


class TraceCoordinates(models.Model):
    dtype = models.CharField(max_length=93)
    root = models.CharField(primary_key=True, max_length=765)
    coordinates = models.CharField(max_length=4000, blank=True, null=True)
    x = models.IntegerField()
    y = models.IntegerField()
    zoomfactor = models.FloatField()
    cktnodeid = models.ForeignKey(CircuitBsTbl, db_column='cktnodeid', blank=True, null=True)
    cktuniqueid = models.ForeignKey(CircuitBsTbl, db_column='cktuniqueid', blank=True, null=True)
    linkid = models.ForeignKey(LinkTable, db_column='linkid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trace_coordinates'


class TransactionLogTable(models.Model):
    transid = models.BigIntegerField(primary_key=True)
    nedbaccessid = models.ForeignKey(NeInfoTable, db_column='nedbaccessid', blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    result = models.NullBooleanField()
    parms = models.CharField(max_length=2048, blank=True, null=True)
    module = models.IntegerField(blank=True, null=True)
    logmessage = models.CharField(max_length=1024, blank=True, null=True)
    service = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_log_table'


class UnmanagedNeInventoryTable(models.Model):
    nedbaccessid = models.IntegerField(primary_key=True)
    serialnumber = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unmanaged_ne_inventory_table'


class UserMapTable(models.Model):
    userid = models.IntegerField()
    treenodetype = models.BooleanField()
    grouporneid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_map_table'
        unique_together = (('userid', 'treenodetype', 'grouporneid'),)


class UserNeTable(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    grouporneid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ne_table'


class UserPreferenceTable(models.Model):
    username = models.CharField(max_length=64)
    clientmodule = models.IntegerField()
    autorefresh = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'user_preference_table'
        unique_together = (('username', 'clientmodule'),)


class UserPreferences(models.Model):
    userpreferenceid = models.IntegerField(primary_key=True)
    socksdefaultid = models.ForeignKey(Socks, db_column='socksdefaultid', blank=True, null=True)
    themesettings = models.CharField(max_length=765, blank=True, null=True)
    userid = models.ForeignKey('UserTable', db_column='userid', unique=True)

    class Meta:
        managed = False
        db_table = 'user_preferences'


class UserTable(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=64)
    userpassword = models.TextField(blank=True, null=True)  # This field type is a guess.
    typeofuser = models.NullBooleanField()
    subtypeofuser = models.IntegerField(blank=True, null=True)
    areaname = models.CharField(max_length=64, blank=True, null=True)
    lastlogintime = models.DateField(blank=True, null=True)
    userlogindisabled = models.NullBooleanField()
    userdescription = models.CharField(max_length=256, blank=True, null=True)
    cmsuser = models.CharField(max_length=64, blank=True, null=True)
    cmspassword = models.CharField(max_length=64, blank=True, null=True)
    failedattempts = models.NullBooleanField()
    statusofuser = models.NullBooleanField()
    passwordsettime = models.DateField(blank=True, null=True)
    lastloginfailtime = models.DateField(blank=True, null=True)
    lockedstate = models.NullBooleanField()
    propagatetone = models.NullBooleanField()
    enablepswdchange = models.NullBooleanField()
    firstuse = models.NullBooleanField()
    usegloballockout = models.NullBooleanField()
    lockoutenabled = models.NullBooleanField()
    lockoutperiod = models.CharField(max_length=3, blank=True, null=True)
    usegloballogout = models.NullBooleanField()
    logoutenabled = models.NullBooleanField()
    logoutperiod = models.CharField(max_length=4, blank=True, null=True)
    enablemultiplelogin = models.IntegerField(blank=True, null=True)
    autodisableinterval = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_table'


class UserTypeTable(models.Model):
    usertypeid = models.IntegerField(primary_key=True)
    usertypename = models.CharField(max_length=64)
    properties = models.NullBooleanField()
    description = models.CharField(max_length=256, blank=True, null=True)
    isdefault = models.NullBooleanField()
    stateenabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'user_type_table'


class VersionTable(models.Model):
    netype = models.IntegerField()
    softwareversion = models.CharField(max_length=128)
    nemodelindex = models.IntegerField()
    nemodelfeatures = models.CharField(max_length=2, blank=True, null=True)
    modelname = models.CharField(max_length=50)
    factorydefault = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'version_table'
        unique_together = (('netype', 'softwareversion', 'nemodelindex'),)


class WavelengthTable(models.Model):
    alias = models.CharField(max_length=4000)
    ctcstring = models.CharField(max_length=4000)
    ctcvalue = models.IntegerField(primary_key=True)
    oddeven = models.IntegerField()
    lcband = models.IntegerField()
    channel32 = models.IntegerField()
    channel40 = models.IntegerField()
    freq = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'wavelength_table'


class WavemuxNe(models.Model):
    neid = models.IntegerField()
    connectiontimeout = models.IntegerField(blank=True, null=True)
    sntpserveripaddr = models.TextField(blank=True, null=True)  # This field type is a guess.
    sntppollingtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wavemux_ne'


class XmlParserStaticTreeTable(models.Model):
    modelindex = models.IntegerField()
    treeindex = models.IntegerField()
    nodeindex = models.IntegerField()
    parentindex = models.IntegerField()
    nodename = models.CharField(max_length=128)
    nodevalue = models.CharField(max_length=128, blank=True, null=True)
    ctmattributename = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xml_parser_static_tree_table'
        unique_together = (('modelindex', 'treeindex', 'nodeindex'),)
