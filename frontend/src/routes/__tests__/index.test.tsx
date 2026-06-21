import { render, screen } from '../../utils/testUtils';
import { Home } from '..';

test('loads and displays greeting', () => {
  render(<Home />);

  const welcomeMessage = screen.getByText(/Welcome!/i);

  expect(welcomeMessage).toBeInTheDocument();
});
