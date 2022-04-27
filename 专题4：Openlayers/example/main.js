import 'ol/ol.css';
import Map from 'ol/Map';
import TileLayer from 'ol/layer/Tile';
import View from 'ol/View';
import {OSM, TileArcGISRest} from 'ol/source';

const url =
  'https://sampleserver1.arcgisonline.com/ArcGIS/rest/services/' +
  'Specialty/ESRI_StateCityHighway_USA/MapServer';

const layers = [
  new TileLayer({
    source: new OSM(),
  }),
  new TileLayer({
    extent: [-13884991, 2870341, -7455066, 6338219],
    source: new TileArcGISRest({
      url: url,
    }),
  }),
];
const map = new Map({
  layers: layers,
  target: 'map',
  view: new View({
    center: [-10997148, 4569099],
    zoom: 4,
  }),
});
