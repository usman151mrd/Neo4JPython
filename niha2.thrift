namespace csharp NiHAThrift
namespace py niha_thrift

enum TEPhylogenticType {
        AS_SYSTEM_TYPE,
        OPERATOR,
        SPECIAL_CHAR,
        PUNCTUATIONS,
        MULTIMEDIA,
        IMAGE,
        AUDIO,
        AUDIO_LINGUAL,
        LINGUAL,
        NODE,
        EDGE,
        GRAPH,
        CONCEPT,
        INSTANCE,
        PROPOSITION,
        RULE,
        PLACE,
        NAME,
        DATETIME,
        COMPANY,
        COLOR,
        MODEL,
        DATAFRAME,
        ROS_MSG_CUSTOM,
        ROS_MSG_GOALD,
        MAP,
        BATTERY_STATUS,
        LINGUAL_PERCEPTION,
        ROS_MSG_GoalStatusArray,
        ROS_MSG_AnalogIOState,
        ROS_MSG_AnalogIOStates,
        ROS_MSG_AnalogOutputCommand,
        ROS_MSG_AssemblyState,
        ROS_MSG_AssemblyStates,
        ROS_MSG_CameraControl,
        ROS_MSG_CameraSetting,
        ROS_MSG_CollisionAvoidanceStat,
        ROS_MSG_CollisionDetectionState,
        ROS_MSG_DigitalIOState,
        ROS_MSG_DigitalIOStates,
        ROS_MSG_DigitalOutputCommand,
        ROS_MSG_EndEffectorCommand,
        ROS_MSG_EndEffectorProperties,
        ROS_MSG_EndEffectorState,
        ROS_MSG_EndPointState,
        ROS_MSG_EndPointStates,
        ROS_MSG_HeadPanCommand,
        ROS_MSG_HeadState,
        ROS_MSG_ITBState,
        ROS_MSG_ITBStates,
        ROS_MSG_JointCommand,
        ROS_MSG_NavigatorState,
        ROS_MSG_NavigatorStates,
        ROS_MSG_RobustControllerStatus,
        ROS_MSG_SEAJointState,
        ROS_MSG_FollowJointTrajectoryAction,
        ROS_MSG_FollowJointTrajectoryActionFeedback,
        ROS_MSG_FollowJointTrajectoryActionGoal,
        ROS_MSG_FollowJointTrajectoryActionResult,
        ROS_MSG_FollowJointTrajectoryFeedback,
        ROS_MSG_FollowJointTrajectoryGoal,
        ROS_MSG_FollowJointTrajectoryResult,
        ROS_MSG_GripperCommand,
        ROS_MSG_GripperCommandAction,
        ROS_MSG_GripperCommandActionFeedback
}


enum TESystemLevelType {
    INT16,  
    INT32, 
    INT64,
    DOUBLE,
    BOOL,
    STRING,
    DATETIME,
    IMAGE,
    AUDIO,
    VIDEO,
    GRAPH,
    DATAFILE,
    DATASOURCE
}   

enum TEAbstractionLevel
{
    SEMANTIC_NODE,
    CONCEPT_NODE,
    INSTANCE_NODE,
}

enum TERepresentationType
{
    SEMANTIC_NETWORK,
    CONCEPTUAL_GRAPH
}

struct TDimension
{
    1: string Neo4jID;    
    2: required string Name; //As label. Will only have only one label
    3: required TESystemLevelType SystemLevelType;//as property
    4: required string Value;//as property
}

struct TFile
{
    1: required string FilePath;
    2: required string FileType;
}

struct TJobType
{
    1: string Neo4jID;    
    2: required string Name;
    3: set<TFile>  Attachments;
    4: set<string> CodeletsToBeUsed;
    5: set<string> SensorsToBeUsed;
    6: set<string> ActuatorsToBeUsed;
}

struct TJob
{
    1: string Neo4jID; 
    2: TJobType JobType;
    3: string JobID;   
    4: required string ScheduledDateTime;
    5: required string DueDateTime;
    6: required i16 PriorityLevel;
}

struct TNode
{
    //CREATE (node:label1:label2:label3...{ key1: value, key2: value, . . . . . . . . .  })
    1: string Neo4jID; 
    2: required string AoKID;//as property
    3: required set<string> Labels; //as label, it will be first label in Labels. example 'fullname'
    4: required string Value; //as property, example 'value:wajahat', the key will be value
    5: required TESystemLevelType SystemLevelType;//as property, example 'SystemType:INT16' as enum number value
    6: required TEAbstractionLevel AbstractionLevel;//
    7: string Tag;//as property, example 'tag:....'
    8: string Validity;//as property, example 'validity: Not > 20'
    9: string ProcessingTag;//as property
    10: set<string> Domains;//
    11: map<string, double> TruthValue;//as property
    12: double Evaluation;//as property
    13: string DateTimeStamp; //as property
    14: i64 AgeInMilliseconds;//as property
    15: double AttentionLevel;
}

struct TRelation
{
    1: string Neo4jID;
    2: string AoKID;
    3: set<string> Labels;
    4: string RelationType; //Domain
    5: TNode SourceNode;
    6: TNode TargetNode;
    7: map<string, TDimension> Properties;
    8: double AttentionLevel;
    10: map<string, double> TruthValue;//as property
}

struct TGraph
{
    1: string Neo4jID;
    2: string ID;
    3: map<string, TNode> Nodes;
    4: map<string, TRelation> Relations;
    5: TERepresentationType RepresentationType;
}

struct TMemoryChunk
{
    1: required string Neo4jID;
    2: string ID;
    3: required string TimeStamp;
    4: TGraph Graph;
    5: required i16 Capacity;
    6: double AttentionLevel;
    7: double DecayLevel;//-1
    8: double Importance;
    9: double Evaluation;
}

struct TCognitiveMemory
{
    1: string Memory;
    2: string ID;
    3: i16 Capacity;
    4: map<string, TMemoryChunk> MemoryChunks;
    5: bool IsDecayable;
    6: map<string,TDimension> Scratchpad;
}

struct TSensoryMotorState
{
    1: double Activation;
    2: bool Enabled;
    3: bool HasStarted;
    4: bool IsActive;
    5: string Name;
    6: string ThreadName
    7: double Threshold;
    8: double AttentionPriorityLevel;
    9: double AttentionLevel;
    10: i16 Frequency;
    11: string Calibration;
}

struct TCodeletState
{
    1: double Activation;
    2: i32 EnableCount;
    3: bool Enabled;
    4: bool HasStarted;
    5: bool IsActive;
    6: bool IsLoop;
    7: i64 LastStartTime;
    8: string Name;
    9: bool ShouldLoop;
    10: string ThreadName
    11: double Threshold;
    12: i64 TimeStep;
    13: double AttentionPriorityLevel;
    14: double AttentionLevel;
}

struct TProgressStatus
{
    1: string Source;
    2: string Status;
    3: double Progress;
}

struct TUser
{
    1: string UserID;
    2: string UserName;
    3: string AppKey;
    4: list<string> RegisteredDevices
}

struct TEndPoint
{
    1: required string Host;
    2: required i32 Port;
    3: required string NodeName;
}

enum TESiginStatus
{
    SIGNIN_SUCCESSFUL,
    SIGNIN_NOT_SUCCESSFUL,
}

service TNiHAEnvironment
{
    TESiginStatus UserSignin(1:TUser user, 2: TEndPoint user_env_endpoint);
    void UserSignOut();
    void UserRegisterDevice(1:string device);
    void Init();
}

service TNiHAUserEnvironment
{

    void Init();
    void ShowMessage(1: string source, 2: string msg);

    //Events
    void OnSignin(1: TUser user, 2: TEndPoint device_endpoint);
    void OnSignOut();

    //void OnSensorAdded(1: string sensor),
    //void OnSensorRemoved(1: string sensor),
    //void OnActuatorAdded(1: string actuator),
    //void OnActuatorRemoved(1: string actuator),


    //Log
    void LogInfo(1:string source, 2:string info);
    void LogException(1:string source, 2:string exp);
    void LogFatal(1:string source, 2:string fatal);
    void LogWarning(1:string source, 2:string warning);
    void LogProgress(1:string source, 2:TProgressStatus progress);
    void LogSensorState(1:string sensorid, 2:TSensoryMotorState state);
    void LogActuatorState(1:string actuatorid, 2:TSensoryMotorState state);
    void LogCodeletState(1:string codeletid, 2:TCodeletState state);
}

service TNOS
{
    TEndPoint GetEndPoint(1:string nodeid);
    map<string, TEndPoint> GetEndPoints()
}

service TNiHAPrimaryBody
{
    void Say(1:string msg);
}

service TNiHASpeechToText
{
    string GetText();
}

service TNiHAFaceRecognition
{
    string Recognize(1: string image_file);
}

service Neo4Niha
{
    string createNode(1: TNode node);
    #TNode retrieveById(1: string neo4jId);
    TNode retrieveNode(1: string query);
    #TNode retrieve();
    bool updateNode(1: TNode node, 2: string neo4Id);
    bool deleteNode(1: string neo4Id);

    string createRelation(1: TRelation relation);
    TRelation retrieveByIdRelation(1: string neo4jId);
    TRelation retrieveRelation(1: string query);
    #TRelation retrieve();
    bool updateRelation(1: TRelation relation, 2: string neo4Id);
    bool deleteRelation(1: string neo4Id);

    string createGraph(1: TGraph graph);
    TGraph retrieveByIdGraph(1: string neo4jId);
    TGraph retrieveGraph(1: string query);
    #TGraph retrieve();
    bool updateGraph(1: TGraph graph, 2: string neo4Id);
    bool deleteGraph(1: string neo4Id);

    string createMemoryChunk(1: TMemoryChunk memoryChunk);
    TMemoryChunk retrieveByIdMemoryChunk(1: string neo4jId);
    TMemoryChunk retrieveMemoryChunk(1: string query);
    #TMemoryChunk retrieve();
    bool updateMemoryChunk(1: TMemoryChunk memoryChunk, 2: string neo4Id);
    bool deleteMemoryChunk(1: string neo4Id);

}
