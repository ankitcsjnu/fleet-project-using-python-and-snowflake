create or replace database Fleet_db;
use database Fleet_db;

create or replace schema raw; 

create or replace file format FF_CSV
Type = CSV
Skip_Header = 1
FIELD_OPTIONALLY_ENCLOSED_BY = '"'
NULL_IF = ('NULL','null','');

create or replace file format FF_JSON
TYPE = json
Compression = auto; -- file mera telemetry.json.gz hai -> Snowflake pehle unzip karta h phir JSON read karta h 

-- i am creating vechile stage here 

create or replace stage VEHICLE_STAGE
URL='s3://fleet-data-buckett/vehicles/'
CREDENTIALS=(
AWS_KEY_ID = 'AKIA4JKAKE2JSOU3Q7MH',
AWS_SECRET_KEY = 'Oe6guYyBpx0KeEno1EJ+uU0skq3aho8o2y7SZzs+'
  )
file_format=FF_CSV;

-- i am creating telementry stage
create or replace stage TELEMETRY_STAGE
URL='s3://fleet-data-buckett/telemetry/'
CREDENTIALS=(
AWS_KEY_ID = 'AKIA4JKAKE2JSOU3Q7MH',
AWS_SECRET_KEY = 'Oe6guYyBpx0KeEno1EJ+uU0skq3aho8o2y7SZzs+'
  )
file_format=ff_json;

-- i am creating Maintenance
create or replace stage MAINT_STAGE
URL='s3://fleet-data-buckett/maintenance/'
CREDENTIALS=(
AWS_KEY_ID = 'Aws key id',
AWS_SECRET_KEY = 'aws secret id'
  )
file_format=FF_CSV;


list @VEHICLE_STAGE;
list @TELEMETRY_STAGE;
list @MAINT_STAGE; 

use schema raw;

create or replace table bronze_raw_Vehicle (  -- total- 11 col in csv file 
    vehicle_id  string,
    vin  string,
    registration_no  string,
    make   string,
    model string,
    year   NUMBER,
    depot string,
    status string,
    odometer_km number,
    fuel_type string,
    last_updated  date
);
copy into  bronze_raw_Vehicle
from @FLEET_DB.PUBLIC.VEHICLE_STAGE
FILE_FORMAT = (FORMAT_NAME = FF_CSV)
ON_ERROR = CONTINUE;

SELECT * FROM FLEET_DB.RAW.BRONZE_RAW_VEHICLE;

