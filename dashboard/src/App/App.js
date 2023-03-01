
import MenuLayout from './../Layout/MenuLayout'
import MenuLayoutLeft from './../Layout/MenuLayoutLeft'
import ListProductItem from './../components/product/ListProductItem'
import './App.css'
function App() {
  return (
    <div className="App">
      <MenuLayout className="mt-0" />
      <MenuLayoutLeft />
      <ListProductItem />
    </div>
  );
}

export default App;
