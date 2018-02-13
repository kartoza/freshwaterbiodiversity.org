--
--
-- Dropping unwanted columns for the site table
--
--


-- Dropping column -- oldsitecode -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: oldsitecode
ALTER TABLE site DROP COLUMN oldsitecode;

-- Dropping column -- projectsitenumber -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: projectsitenumber
ALTER TABLE site DROP COLUMN projectsitenumber;

-- Dropping column -- longitudinalzoneid -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: longitudinalzoneid
ALTER TABLE site DROP COLUMN longitudinalzoneid;

-- Dropping column -- reference -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: reference
ALTER TABLE site DROP COLUMN reference;

-- Dropping column -- mapreference -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: mapreference
ALTER TABLE site DROP COLUMN mapreference;

-- Dropping column -- contrangefrom -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: contrangefrom
ALTER TABLE site DROP COLUMN contrangefrom;

-- Dropping column -- contrangeto -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: contrangeto
ALTER TABLE site DROP COLUMN contrangeto;

-- Dropping column -- sitelength -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: sitelength
ALTER TABLE site DROP COLUMN sitelength;

-- Dropping column -- Source -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: Source
ALTER TABLE site DROP COLUMN "Source";

-- Dropping column -- hydrotypeid -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: hydrotypeid
ALTER TABLE site DROP COLUMN hydrotypeid;

-- Dropping column -- hydrotypenaturalid -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: hydrotypenaturalid
ALTER TABLE site DROP COLUMN hydrotypenaturalid;

-- Dropping column -- gaugingstation -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: gaugingstation
ALTER TABLE site DROP COLUMN gaugingstation;

-- Dropping column -- dwafcode -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: dwafcode
ALTER TABLE site DROP COLUMN dwafcode;

-- Dropping column -- distup -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: distup
ALTER TABLE site DROP COLUMN distup;

-- Dropping column -- distdown -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: distdown
ALTER TABLE site DROP COLUMN distdown;

-- Dropping column -- assossysid -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: assossysid
ALTER TABLE site DROP COLUMN assossysid;

-- Dropping column -- assocsysdist -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: assocsysdist
ALTER TABLE site DROP COLUMN assocsysdist;

-- Dropping column -- assocsysname -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: assocsysname
ALTER TABLE site DROP COLUMN assocsysname;

-- Dropping column -- Notify -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: Notify
ALTER TABLE site DROP COLUMN "Notify";

-- Dropping column -- permitrequired -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: permitrequired
ALTER TABLE site DROP COLUMN permitrequired;

-- Dropping column -- permitdetails -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: permitdetails
ALTER TABLE site DROP COLUMN permitdetails;

-- Dropping column -- permitacquired -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: permitacquired
ALTER TABLE site DROP COLUMN permitacquired;

-- Dropping column -- validityofpermit -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: validityofpermit
ALTER TABLE site DROP COLUMN validityofpermit;

-- Dropping column -- Key -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: Key
ALTER TABLE site DROP COLUMN "Key";

-- Dropping column -- keyavailability -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: keyavailability
ALTER TABLE site DROP COLUMN keyavailability;

-- Dropping column -- farm -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: farm
ALTER TABLE site DROP COLUMN farm;

-- Dropping column -- farmregistrationcode -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: farmregistrationcode
ALTER TABLE site DROP COLUMN farmregistrationcode;

-- Dropping column -- georeferencecomment -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: georeferencecomment
ALTER TABLE site DROP COLUMN georeferencecomment;

-- Dropping column -- mapprojection -- on table -- site -- as it is marked for deletion
-- in the database specification document
-- Column: mapprojection
ALTER TABLE site DROP COLUMN mapprojection;


--
--
-- Dropping unwanted columns for the sitevisit table
--


-- Dropping column -- Time -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: Time
ALTER TABLE sitevisit DROP COLUMN "Time";

-- Dropping column -- rain -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: rain
ALTER TABLE sitevisit DROP COLUMN rain;

-- Dropping column -- raincomment -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: raincomment
ALTER TABLE sitevisit DROP COLUMN raincomment;

-- Dropping column -- embeddednessid -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: embeddednessid
ALTER TABLE sitevisit DROP COLUMN embeddednessid;

-- Dropping column -- fastflow -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: fastflow
ALTER TABLE sitevisit DROP COLUMN fastflow;

-- Dropping column -- fastflowname -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: fastflowname
ALTER TABLE sitevisit DROP COLUMN fastflowname;

-- Dropping column -- waterfiltered -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: waterfiltered
ALTER TABLE sitevisit DROP COLUMN waterfiltered;

-- Dropping column -- volfiltered -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: volfiltered
ALTER TABLE sitevisit DROP COLUMN volfiltered;

-- Dropping column -- samples -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: samples
ALTER TABLE sitevisit DROP COLUMN samples;

-- Dropping column -- analysis -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: analysis
ALTER TABLE sitevisit DROP COLUMN analysis;

-- Dropping column -- frozen -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: frozen
ALTER TABLE sitevisit DROP COLUMN frozen;

-- Dropping column -- prev -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: prev
ALTER TABLE sitevisit DROP COLUMN prev;

-- Dropping column -- sampleinstitute -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: sampleinstitute
ALTER TABLE sitevisit DROP COLUMN sampleinstitute;

-- Dropping column -- canopycovercomment -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: canopycovercomment
ALTER TABLE sitevisit DROP COLUMN canopycovercomment;

-- Dropping column -- habitatintegritycomment -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: habitatintegritycomment
ALTER TABLE sitevisit DROP COLUMN habitatintegritycomment;

-- Dropping column -- sassdatacomment -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: sassdatacomment
ALTER TABLE sitevisit DROP COLUMN sassdatacomment;

-- Dropping column -- fishowner -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: fishowner
ALTER TABLE sitevisit DROP COLUMN fishowner;

-- Dropping column -- fishassessor -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: fishassessor
ALTER TABLE sitevisit DROP COLUMN fishassessor;

-- Dropping column -- ripirianowner -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: ripirianowner
ALTER TABLE sitevisit DROP COLUMN ripirianowner;

-- Dropping column -- ripirianassessor -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: ripirianassessor
ALTER TABLE sitevisit DROP COLUMN ripirianassessor;

-- Dropping column -- waterchemistryowner -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: waterchemistryowner
ALTER TABLE sitevisit DROP COLUMN waterchemistryowner;

-- Dropping column -- waterchemistryassessor -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: waterchemistryassessor
ALTER TABLE sitevisit DROP COLUMN waterchemistryassessor;

-- Dropping column -- channeltypeid -- on table -- sitevisit -- as it is marked for deletion
-- in the database specification document
-- Column: channeltypeid
ALTER TABLE sitevisit DROP COLUMN channeltypeid;



--
--
-- Dropping unwanted tables
--
--


-- Dropping table  -- archived_channeldescription -- as it is marked for deletion
-- in the database specification document
-- Table: archived_channeldescription
DROP TABLE archived_channeldescription;

-- Dropping table  -- archived_chemistry_generalinformation -- as it is marked for deletion
-- in the database specification document
-- Table: archived_chemistry_generalinformation
DROP TABLE archived_chemistry_generalinformation;

-- Dropping table  -- archived_geomorphology -- as it is marked for deletion
-- in the database specification document
-- Table: archived_geomorphology
DROP TABLE archived_geomorphology;

-- Dropping table  -- archived_habitatassessmentham_hqi -- as it is marked for deletion
-- in the database specification document
-- Table: archived_habitatassessmentham_hqi
DROP TABLE archived_habitatassessmentham_hqi;

-- Dropping table  -- archived_indexofhabitatintegrity -- as it is marked for deletion
-- in the database specification document
-- Table: archived_indexofhabitatintegrity
DROP TABLE archived_indexofhabitatintegrity;

-- Dropping table  -- archived_riparianvegetationindex -- as it is marked for deletion
-- in the database specification document
-- Table: archived_riparianvegetationindex
DROP TABLE archived_riparianvegetationindex;

-- Dropping table  -- archived_riparianzonedescription -- as it is marked for deletion
-- in the database specification document
-- Table: archived_riparianzonedescription
DROP TABLE archived_riparianzonedescription;

-- Dropping table  -- archived_sitecondition -- as it is marked for deletion
-- in the database specification document
-- Table: archived_sitecondition
DROP TABLE archived_sitecondition;

-- Dropping table  -- archived_speciesrichness -- as it is marked for deletion
-- in the database specification document
-- Table: archived_speciesrichness
DROP TABLE archived_speciesrichness;

-- Dropping table  -- archived_vegetationcover -- as it is marked for deletion
-- in the database specification
-- Table: archived_vegetationcover
DROP TABLE archived_vegetationcover;

-- Dropping table  -- archived_vegetationdistribution -- as it is marked for deletion
-- in the database specification document
-- Table: archived_vegetationdistribution
DROP TABLE archived_vegetationdistribution;

-- Dropping table  -- archived_vegetationinvasion -- as it is marked for deletion
-- in the database specification document
-- Table: archived_vegetationinvasion
DROP TABLE archived_vegetationinvasion;

-- Dropping table  -- table -- archived_vegetationspecieslist -- as it is marked for deletion
-- in the database specification document
-- Table: archived_vegetationspecieslist
DROP TABLE archived_vegetationspecieslist;


-- Dropping table  -- temp_view_archived_chemistry_generalinformation -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_archived_chemistry_generalinformation
DROP TABLE temp_view_archived_chemistry_generalinformation;

-- Dropping table  -- temp_view_archived_riparianvegetationindex -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_archived_riparianvegetationindex
DROP TABLE temp_view_archived_riparianvegetationindex;

-- Dropping table  -- temp_view_archiveddata -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_archiveddata
DROP TABLE temp_view_archiveddata;

-- Dropping table  -- temp_view_indexofhabitatintegrity -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_indexofhabitatintegrity
DROP TABLE temp_view_indexofhabitatintegrity;

-- Dropping table  -- temp_view_sitegeomorphology -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitegeomorphology
DROP TABLE temp_view_sitegeomorphology;

-- Dropping table  -- temp_view_sitegeoreference -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitegeoreference
DROP TABLE temp_view_sitegeoreference;

-- Dropping table  -- temp_view_siteinformationgeneral -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_siteinformationgeneral
DROP TABLE temp_view_siteinformationgeneral;

-- Dropping table  -- temp_view_siteinformationlocation -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_siteinformationlocation
DROP TABLE temp_view_siteinformationlocation;

-- Dropping table  -- temp_view_siteinformationregional -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_siteinformationregional
DROP TABLE temp_view_siteinformationregional;

-- Dropping table  -- temp_view_sitevisitbiotopeinvertebrates -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopeinvertebrates
DROP TABLE temp_view_sitevisitbiotopeinvertebrates;

-- Dropping table  -- temp_view_sitevisitbiotopeinvertebratesxtababundance -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopeinvertebratesxtababundance
DROP TABLE temp_view_sitevisitbiotopeinvertebratesxtababundance;

-- Dropping table  -- temp_view_sitevisitbiotopeinvertebratesxtababundancesass4 -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopeinvertebratesxtababundancesass4
DROP TABLE temp_view_sitevisitbiotopeinvertebratesxtababundancesass4;

-- Dropping table  -- temp_view_sitevisitbiotopeinvertebratesxtababundancesass5 -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopeinvertebratesxtababundancesass5
DROP TABLE temp_view_sitevisitbiotopeinvertebratesxtababundancesass5;

-- Dropping table  -- temp_view_sitevisitbiotopeinvertebratesxtabscore -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopeinvertebratesxtabscore
DROP TABLE temp_view_sitevisitbiotopeinvertebratesxtabscore;

-- Dropping table  -- temp_view_sitevisitbiotopeinvertebratesxtabscoresass4 -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopeinvertebratesxtabscoresass4
DROP TABLE temp_view_sitevisitbiotopeinvertebratesxtabscoresass4;

-- Dropping table  -- temp_view_sitevisitbiotopeinvertebratesxtabscoresass5 -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopeinvertebratesxtabscoresass5
DROP TABLE temp_view_sitevisitbiotopeinvertebratesxtabscoresass5;

-- Dropping table  -- temp_view_sitevisitbiotopes -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopes
DROP TABLE temp_view_sitevisitbiotopes;

-- Dropping table  -- temp_view_sitevisitbiotopesass_scores -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitbiotopesass_scores
DROP TABLE temp_view_sitevisitbiotopesass_scores;

-- Dropping table  -- temp_view_sitevisitchannelmodifications -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitchannelmodifications
DROP TABLE temp_view_sitevisitchannelmodifications;

-- Dropping table  -- temp_view_sitevisitchannelmorphology -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitchannelmorphology
DROP TABLE temp_view_sitevisitchannelmorphology;

-- Dropping table  -- temp_view_sitevisitchemistry -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitchemistry
DROP TABLE temp_view_sitevisitchemistry;

-- Dropping table  -- temp_view_sitevisitchemistrygeneralinformation -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitchemistrygeneralinformation
DROP TABLE temp_view_sitevisitchemistrygeneralinformation;

-- Dropping table  -- temp_view_sitevisitchemistryxtab -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitchemistryxtab
DROP TABLE temp_view_sitevisitchemistryxtab;

-- Dropping table  -- temp_view_sitevisitfishdatahabitatcover -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitfishdatahabitatcover
DROP TABLE temp_view_sitevisitfishdatahabitatcover;

-- Dropping table  -- temp_view_sitevisitfishsampledetail -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitfishsampledetail
DROP TABLE temp_view_sitevisitfishsampledetail;

-- Dropping table  -- temp_view_sitevisitgeomorphology -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitgeomorphology
DROP TABLE temp_view_sitevisitgeomorphology;

-- Dropping table  -- temp_view_sitevisitgeoreference -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitgeoreference
DROP TABLE temp_view_sitevisitgeoreference;

-- Dropping table  -- temp_view_sitevisithabitatassessment -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisithabitatassessment
DROP TABLE temp_view_sitevisithabitatassessment;

-- Dropping table  -- temp_view_sitevisitihas -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitihas
DROP TABLE temp_view_sitevisitihas;

-- Dropping table  -- temp_view_sitevisitinformationgeneral -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitinformationgeneral
DROP TABLE temp_view_sitevisitinformationgeneral;

-- Dropping table  -- temp_view_sitevisitinformationlocation -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitinformationlocation
DROP TABLE temp_view_sitevisitinformationlocation;

-- Dropping table  -- temp_view_sitevisitinformationregional -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitinformationregional
DROP TABLE temp_view_sitevisitinformationregional;

-- Dropping table  -- temp_view_sitevisitinvertebrates -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitinvertebrates
DROP TABLE temp_view_sitevisitinvertebrates;

-- Dropping table  -- temp_view_sitevisitlanduse -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitlanduse
DROP TABLE temp_view_sitevisitlanduse;

-- Dropping table  -- temp_view_sitevisitsamplingoccasiongeneralinformation -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitsamplingoccasiongeneralinformation
DROP TABLE temp_view_sitevisitsamplingoccasiongeneralinformation;

-- Dropping table  -- temp_view_sitevisitsass_scores -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitsass_scores
DROP TABLE temp_view_sitevisitsass_scores;

-- Dropping table  -- temp_view_sitevisitsassbiotopes -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitsassbiotopes
DROP TABLE temp_view_sitevisitsassbiotopes;

-- Dropping table  -- temp_view_sitevisitstreamdimension -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitstreamdimension
DROP TABLE temp_view_sitevisitstreamdimension;

-- Dropping table  -- temp_view_sitevisitsubstratum -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisitsubstratum
DROP TABLE temp_view_sitevisitsubstratum;

-- Dropping table  -- temp_view_sitevisittaxonxtababundance -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisittaxonxtababundance
DROP TABLE temp_view_sitevisittaxonxtababundance;

-- Dropping table  -- temp_view_sitevisittaxonxtababundancesass4 -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisittaxonxtababundancesass4
DROP TABLE temp_view_sitevisittaxonxtababundancesass4;

-- Dropping table  -- temp_view_sitevisittaxonxtababundancesass5 -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisittaxonxtababundancesass5
DROP TABLE temp_view_sitevisittaxonxtababundancesass5;

-- Dropping table  -- temp_view_sitevisittaxonxtabscore -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisittaxonxtabscore
DROP TABLE temp_view_sitevisittaxonxtabscore;

-- Dropping table  -- temp_view_sitevisittaxonxtabscoresass4 -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisittaxonxtabscoresass4
DROP TABLE temp_view_sitevisittaxonxtabscoresass4;

-- Dropping table  -- temp_view_sitevisittaxonxtabscoresass5 -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_sitevisittaxonxtabscoresass5
DROP TABLE temp_view_sitevisittaxonxtabscoresass5;

-- Dropping table  -- temp_view_subregion -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_subregion
DROP TABLE temp_view_subregion;

-- Dropping table  -- temp_view_summarizedrivermakeup -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_summarizedrivermakeup
DROP TABLE temp_view_summarizedrivermakeup;

-- Dropping table  -- temp_view_user -- as it is marked for deletion
-- in the database specification document
-- Table: temp_view_user
DROP TABLE temp_view_user;


-- Dropping table -- assossys -- as it is marked for deletion
-- in the database specification documant
-- Table: assossys
DROP TABLE assossys;

-- Dropping table -- bankmods -- as it is marked for deletion
-- in the database specification documant
-- we need to drop the dependent columns connecting this table first
ALTER TABLE sitevisitbankmod DROP COLUMN bankmodsid;
-- Table: bankmods
DROP TABLE bankmods;

-- Dropping table -- channeltype -- as it is marked for deletion
-- in the database specification documant
-- Table: channeltype
DROP TABLE channeltype;

-- Dropping table -- channeltypedetail -- as it is marked for deletion
-- in the database specification documant
-- dependent connection needs to be dropped first
ALTER TABLE sitechanneltypedetail DROP COLUMN channeltypedetailid;

-- Table: channeltypedetail
DROP TABLE channeltypedetail;

-- Dropping table -- cover -- as it is marked for deletion
-- in the database specification documant
-- dependent connection needs to be dropped first
ALTER TABLE fishcoverpreference DROP COLUMN coverid;
ALTER TABLE sitevisitfishhabitatcover DROP COLUMN coverid;

-- Table: cover
DROP TABLE cover;

-- Dropping table -- coverestimate -- as it is marked for deletion
-- in the database specification documant
-- drop dependent connecting column first
ALTER TABLE sitevisitfishhabitatcover DROP COLUMN coverestimateid;
-- Table: coverestimate
DROP TABLE coverestimate;

-- Dropping table -- crosssectionpoint -- as it is marked for deletion
-- in the database specification documant
-- drop dependent connected columns first
ALTER TABLE sitevisitcrosssectionpoint DROP COLUMN crosssectionpointid;
-- Table: crosssectionpoint
DROP TABLE crosssectionpoint;

-- Dropping table -- dataintegritycheckexclude -- as it is marked for deletion
-- in the database specification documant
-- Table: dataintegritycheckexclude
DROP TABLE dataintegritycheckexclude;

-- Dropping table -- embeddedness -- as it is marked for deletion
-- in the database specification documant
-- Table: embeddedness
DROP TABLE embeddedness;

-- Dropping table -- fishcoverpreference -- as it is marked for deletion
-- in the database specification documant
-- Table: fishcoverpreference
DROP TABLE fishcoverpreference;

-- Dropping table -- fishhabitat -- as it is marked for deletion
-- in the database specification documant
-- need to drop dependent connecting columns first
ALTER TABLE fishhabitatpreference DROP COLUMN fishhabitatid;
ALTER TABLE sitevisitfishhabitatcover DROP COLUMN fishhabitatid;
ALTER TABLE sitevisitfishhabitatsample DROP COLUMN fishhabitatid;

-- Table: fishhabitat
DROP TABLE fishhabitat;

-- Dropping table -- fishhabitatpreference -- as it is marked for deletion
-- in the database specification documant
-- Table: fishhabitatpreference
DROP TABLE fishhabitatpreference;

-- Dropping table -- fishhabitatsamplingcatchability -- as it is marked for deletion
-- in the database specification documant
-- Table: fishhabitatsamplingcatchability
--DROP TABLE fishhabitatsamplingcatchability;

-- Dropping table -- fishintolerance -- as it is marked for deletion
-- in the database specification documant
-- Table: fishintolerance
DROP TABLE fishintolerance;

-- Dropping table -- habitattype -- as it is marked for deletion
-- in the database specification documant
-- need to drop dependent columns first
ALTER TABLE sitevisithabitattype DROP COLUMN habitattypeid;

-- Table: habitattype
DROP TABLE habitattype;

-- Dropping table -- hydrotype -- as it is marked for deletion
-- in the database specification documant
-- Table: hydrotype
DROP TABLE hydrotype;

-- Dropping table -- ihicatchment -- as it is marked for deletion
-- in the database specification documant
-- we need to drop the dependent connecting columns first
ALTER TABLE ihisitevisitcatchment DROP COLUMN ihicatchmentid;

-- Table: ihicatchment
DROP TABLE ihicatchment;

-- Dropping table -- ihigeomorphzone -- as it is marked for deletion
-- in the database specification documant
-- we need to first drop the dependent connecting columns
ALTER TABLE ihisitevisitrivertype DROP COLUMN ihigeomorphzoneid;
-- Table: ihigeomorphzone
DROP TABLE ihigeomorphzone;

-- Dropping table -- ihiinstream -- as it is marked for deletion
-- in the database specification documant
-- we need to first drop the dependent connecting columns
ALTER TABLE ihisitevisitinstream DROP COLUMN ihiinstreamid;

-- Table: ihiinstream
DROP TABLE ihiinstream;

-- Dropping table -- ihiinstreamcomponent -- as it is marked for deletion
-- in the database specification documant
-- we need to first drop the dependent connecting columns
ALTER TABLE ihisitevisitinstreamcomponent DROP COLUMN ihiinstreamcomponentid;
-- Table: ihiinstreamcomponent
DROP TABLE ihiinstreamcomponent;

-- Dropping table -- ihiriperianzone -- as it is marked for deletion
-- in the database specification documant
-- we need to first drop the dependent connecting columns
ALTER TABLE ihisitevisitriparianzone DROP COLUMN ihiriparianzoneid;
-- Table: ihiriperianzone
DROP TABLE ihiriparianzone;

-- Dropping table -- ihiriperianzonecomponent -- as it is marked for deletion
-- in the database specification documant
-- we need to first drop the dependent connecting columns
ALTER TABLE ihisitevisitriparianzonecomponent DROP COLUMN ihiriparianzonecomponentid;
-- Table: ihiriparianzonecomponent
DROP TABLE ihiriparianzonecomponent;

-- Dropping table -- ihiseasonality -- as it is marked for deletion
-- in the database specification documant
-- we need to first drop the dependent columns first
ALTER TABLE ihisitevisitseasonality DROP COLUMN ihiseasonalityid;
-- Table: ihiseasonality
DROP TABLE ihiseasonality;

-- Dropping table -- ihisitevisitcatchment -- as it is marked for deletion
-- in the database specification documant
-- Table: ihisitevisitcatchment
DROP TABLE ihisitevisitcatchment;

-- Dropping table -- ihisitevisitinstream -- as it is marked for deletion
-- in the database specification documant
-- Table: ihisitevisitinstream
DROP TABLE ihisitevisitinstream;

-- Dropping table -- ihisitevisiteinstreamcomponent -- as it is marked for deletion
-- in the database specification documant
-- Table: ihisitevisitinstreamcomponent
DROP TABLE ihisitevisitinstreamcomponent;

-- Dropping table -- ihisitevisitrivertype -- as it is marked for deletion
-- in the database specification documant
-- Table: ihisitevisitrivertype
DROP TABLE ihisitevisitrivertype;

-- Dropping table -- ihisitevisitseasonality -- as it is marked for deletion
-- in the database specification documant
-- Table: ihisitevisitseasonality
DROP TABLE ihisitevisitseasonality;

-- Dropping table -- ihiwidth -- as it is marked for deletion
-- in the database specification documant
-- Table: ihiwidth
DROP TABLE ihiwidth;

-- Dropping table -- landuse -- as it is marked for deletion
-- in the database specification documant
-- Table: landuse
DROP TABLE landuse;

-- Dropping table -- levelofconfidence -- as it is marked for deletion
-- in the database specification documant
-- we need to drop the dependent connecting columns first
ALTER TABLE sitevisitformulacriterionentry DROP COLUMN levelofconfidenceid;
-- Table: levelofconfidence
DROP TABLE levelofconfidence;

-- Dropping table -- Ripvegimpact - drop -- as it is marked for deletion
-- in the database specification documant
-- we need to drop the dependent connecting columns first
ALTER TABLE sitevisitripvegchannelimpact DROP COLUMN ripvegimpactid;
-- Table: Ripvegimpact
DROP TABLE Ripvegimpact;

-- Dropping table -- rivermakeup -- as it is marked for deletion
-- in the database specification documant
-- we first need to drop the dependent connected columns here
ALTER TABLE sitevisit DROP COLUMN biotope;
-- Table: rivermakeup
DROP TABLE rivermakeup;

-- Dropping table -- Samplingmethod -- as it is marked for deletion
-- in the database specification documant
-- we first need to drop the dependent connected columns here
ALTER TABLE fishhabitatsamplingcatchability DROP COLUMN samplingmethodid;
ALTER TABLE sitevisitfishhabitatsample DROP COLUMN samplingmethodid;
-- Table: Samplingmethod
DROP TABLE Samplingmethod;

-- Dropping table -- Sassbiotopespecificbiotope -- as it is marked for deletion
-- in the database specification documant
-- Table: Sassbiotopespecificbiotope
DROP TABLE Sassbiotopespecificbiotope;

-- Dropping table -- Sitechanneltypedetail -- as it is marked for deletion
-- in the database specification documant
-- Table: Sitechanneltypedetail
DROP TABLE Sitechanneltypedetail;

-- Dropping table -- Sitetransaction -- as it is marked for deletion
-- in the database specification documant
-- Table: Sitetransaction
DROP TABLE Sitetransaction;

-- Dropping table -- Traceriver -- as it is marked for deletion
-- in the database specification documant
-- Table: Traceriver
DROP TABLE Traceriver;
