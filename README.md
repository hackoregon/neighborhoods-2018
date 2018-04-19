# Neighborhoods - 2018

---

## Glossary of Common Terms

- [Types of Data Classification](#types-of-data-classification)

GIS: A geographic information system (GIS) is a framework for gathering, managing, and analyzing data. Rooted in the science of geography, GIS integrates many types of data. It analyzes spatial location and organizes layers of information into visualizations using maps and 3D scenes. ​With this unique capability, GIS reveals deeper insights into data, such as patterns, relationships, and situations—helping users make smarter decisions. 

ArcGIS: A platform for organizations to create, manage, share, and analyze spatial data. It consists of server components, mobile and desktop applications, and developer tools. This platform can be deployed on-premises or in the cloud (Amazon, Azure) with ArcGIS Enterprise, or used via ArcGIS Online which is hosted and managed by Esri.

QGIS: QGIS is a user friendly Open Source Geographic Information System (GIS) licensed under the GNU General Public License. QGIS is an official project of the Open Source Geospatial Foundation (OSGeo). It runs on Linux, Unix, Mac OSX, Windows and Android and supports numerous vector, raster, and database formats and functionalities.

Basemap: This refers to a collection of GIS data and/or orthorectified imagery that form the background setting for a map. The function of the basemap is to provide background detail necessary to orient the location of the map. Basemaps also add to the aesthetic appeal of a map.

Aggregation: Any process in which information is gathered and expressed in a summary form, for purposes such as statistical analysis. A common aggregation purpose is to get more information about particular groups based on specific variables such as age, profession, or income.

Attribute: Specifications that define a properties of an object, element, or file. It may also refer to or set the specific value for a given instance of such. For clarity, attributes should more correctly be considered metadata.

Attribute table: In a GIS, attribute tables are often joined or related to spatial data layers, and the attribute values they contain can be used to find, query, and symbolize features or raster cells.

Shapefile: A popular geospatial vector data format for geographic information system (GIS) software. It is developed and regulated by Esri as a (mostly) open specification for data interoperability among Esri and other GIS software products.

Layer: This represents geographic data in ArcMap, such as a particular theme of data. Example map layers include streams and lakes, terrain, roads, political boundaries, parcels, building footprints, utility lines, and orthophoto imagery

Table of Contents: In ArcGIS, a tabbed list of data frames and layers (or tables) on a map that shows how the data is symbolized, the source of the data, and whether or not each layer is selectable.

Symbology: The set of conventions, rules, or encoding systems that define how geographic features are represented with symbols on a map. A characteristic of a map feature may influence the size, color, and shape of the symbol used.

### Types of Data Classification

- Equal Interval: In this classification, each class occupies an equal interval along the number line. They are found by determining the range of the data. The range is then divided by the number of classes, which gives the common difference.

- Quantile: In this classification, a set of values are distributed into groups that contain an equal number of values. The attribute values are added up, then divided into the predetermined number of classes. Graph showing 10 points in each interval, which makes the intervals uneven sizes.

- Natural Breaks (Jenks): A method of manual data classification that seeks to partition data into classes based on natural groups in the data distribution. Natural breaks occur in the histogram at the low points of valleys.

- Standard Deviation:  A data classification method that finds the mean value, then places class breaks above and below the mean at intervals of either .25, .5, or 1 standard deviation until all the data values are contained within the classes.

- ArcToolbox: is an integrated application developed by Esri. It provides a reference to the toolboxes to facilitate user interface in ArcGIS for accessing and organizing a collection of geoprocessing tools, models and scripts.

- Buffer: A zone around a map feature measured in units of distance or time. A buffer is useful for proximity analysis. A buffer is an area defined by the bounding region determined by a set of points at a specified maximum distance from all nodes along segments of an object.

- Clip: To overlay a polygon on one or more target features (layers) and extract from the target feature (or features) only the target feature data that lies within the area outlined by the clip polygon. In other words, the boundaries of the second polygon are imposed on the first polygon.

- Intersect: An analytical operation that can be used to select any part of a feature that intersects with one or more other features. The areas of the map where all the input features intersect will create a feature as the intersect output.

- Union: Is an analytical process in which the features from two or more map layers are combined into a single, composite layer. Union includes the data from all the included layers, meaning that overlapping and non-overlapping areas are included in a new polygon.

- Merge: This combines selected features of the same layer into one feature. The features must be from either a line or a polygon layer. When merging, you choose which feature's attributes are preserved during the operation.

- Dissolve: This is an application of the conceptual operators that aggregates features often referred to as 'Merge' or 'Amalgamation.' It is a process in which a new map feature is created by merging adjacent polygons, lines, or regions that have a common value for a specified attribute.

- Geographically Weighed Regression: GWR is one of several spatial regression techniques, increasingly used in geography and other disciplines. GWR provides a local model of the variable or process you are trying to understand/predict by fitting a regression equation to every feature in the dataset. GWR constructs these separate equations by incorporating the dependent and explanatory variables of features falling within the bandwidth of each target feature. The shape and size of the bandwidth is dependent on user input for the Kernel Type, Bandwidth Method, Distance, and Number of Features.

- Spatial Selection: This selects features from one layer that fall within or touches an edge of polygon features in a second layer

- Select by Attribute: This allows you to provide a SQL query expression that is used to select features that match the selection criteria.

- Select by Location: This lets you select features based on their location relative to features in another layer. For instance, if you want to know how many homes were affected by a recent flood, you could select all the homes that fall within the flood boundary.

- Erase: An analytical process in which the output feature class is created by copying the portions of the input features that lie outside the boundaries of the erase features.

- Spatial Join: This is a GIS operation that affixes data from one feature layer’s attribute table to another from a spatial perspective.

- Relate: This simply defines a relationship between two tables.

- Point Distance: This tool creates a table with distances between two sets of points.

- Interpolation: This predicts values for cells in a raster from a limited number of sample data points.

- Kernel Density: This calculates the density of features in a neighborhood around those features. It can be calculated for both point and line features.

- Overlay: This is an operation that superimposes multiple data sets (representing different themes) together for the purpose of identifying relationships between them.
